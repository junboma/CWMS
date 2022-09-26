from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
import uuid

class NewUser(AbstractUser):

    role_type = [
        [0, 'admin'],
        [1, 'user'],
    ]

    roles = models.IntegerField(verbose_name='角色', choices=role_type, default=1)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True, auto_now=True)
    code = models.UUIDField(verbose_name='uuid', default=uuid.uuid4, editable=False)

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        pass


class UserProfile(models.Model):
    """
    扩展用户，需要在settings设置认证model
    """
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='姓名', help_text='姓名')
    job_id = models.CharField(max_length=30, blank=True, null=True, verbose_name='工号', help_text='工号')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月', help_text='出生年月')
    mobile = models.CharField(max_length=11, verbose_name='手机号', help_text='手机号')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='male', verbose_name='性别', help_text='性别')
    post = models.ForeignKey(to="Post", verbose_name="关联岗位", on_delete=models.PROTECT, db_constraint=False, null=True, blank=True, help_text="关联岗位")
    # role = models.ManyToManyField(to="Role", verbose_name="关联角色", db_constraint=False, help_text="关联角色")
    CRH = models.ManyToManyField(to="CRH", verbose_name="关联车型资质", db_constraint=False, help_text="关联车型资质")
    dept = models.ForeignKey(
        to="Dept", verbose_name="所属班组", on_delete=models.PROTECT, db_constraint=False, null=True, blank=True, help_text="关联班组"
    )
    workshop = models.ForeignKey(
        to="Workshop", verbose_name="所属车间", on_delete=models.PROTECT, db_constraint=False, null=True, blank=True, help_text="关联车间"
    )
    railway_sections = models.ForeignKey(
        to="Railway_sections", verbose_name="所属站段", on_delete=models.PROTECT, db_constraint=False, null=True, blank=True, help_text="关联站段"
    )
    STATUS_CHOICES = (
        (0, "离职"),
        (1, "在职"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="在职状态", help_text="在职状态")
    is_keypeople = models.BooleanField(default=False, verbose_name="是否为关键人", help_text="是否为关键人")
    def set_password(self, raw_password):
        super().set_password(hashlib.md5(raw_password.encode(encoding="UTF-8")).hexdigest())

    class Meta:
        db_table = "system_users"
        verbose_name_plural = verbose_name = '用户表'
        # ordering = ("-create_datetime",)

    def __str__(self):
        # 要判断name是否有值，如果没有，则返回username，否则使用createsuperuser创建用户访问与用户关联的模型会报错，
        # 页面（A server error occurred. Please contact the administrator.）
        # 后台（UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 9737: illegal multibyte sequence）
        if self.name:
            return self.name
        else:
            return self.username
    # def __str__(self):
    #     return self.name

class Examiner(models.Model):
    name = models.ForeignKey(to="UserProfile", verbose_name="考评人", on_delete=models.PROTECT, db_constraint=False, help_text="考评人")
    sort = models.IntegerField(default=1, verbose_name="考评人顺序", help_text="考评人顺序")

    class Meta:
        db_table = "system_examiner"
        verbose_name = "考评人管理"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    name = models.CharField(null=False, max_length=64, verbose_name="岗位名称", help_text="岗位名称")
    sort = models.IntegerField(default=1, verbose_name="岗位顺序", help_text="岗位顺序")

    class Meta:
        db_table = "system_post"
        verbose_name = "岗位表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return self.name

class CRH(models.Model):
    name = models.CharField(max_length=64, verbose_name="车型资质", help_text="车型资质")
    sort = models.IntegerField(default=1, verbose_name="车型顺序", help_text="车型顺序")
    class Meta:
        db_table = "system_crh"
        verbose_name = "车型表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return self.name

# class Role(models.Model):
#     name = models.CharField(max_length=64, verbose_name="角色名称", help_text="角色名称")
#     sort = models.IntegerField(default=1, verbose_name="角色顺序", help_text="角色顺序")
#     DATASCOPE_CHOICES = (
#         (0, "CRH1A"),
#         (1, "CRH1A-A"),
#         (2, "CRH2A"),
#         (3, "CRH380A"),
#         (4, "CR400"),
#     )
#     data_range = models.IntegerField(default=0, choices=DATASCOPE_CHOICES, verbose_name="车型资质", help_text="车型资质")
#
#
#     class Meta:
#         db_table = "system_role"
#         verbose_name = "角色表"
#         verbose_name_plural = verbose_name
#         ordering = ("sort",)
#
#     def __str__(self):
#         return self.name


class Dept(models.Model):
    name = models.CharField(max_length=64, verbose_name="班组名称", help_text="班组名称")
    sort = models.IntegerField(default=1, verbose_name="显示排序", help_text="显示排序")
    owner = models.CharField(max_length=32, verbose_name="负责人", null=True, blank=True, help_text="负责人")
    phone = models.CharField(max_length=32, verbose_name="联系电话", null=True, blank=True, help_text="联系电话")
    email = models.EmailField(max_length=32, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")
    status = models.BooleanField(default=True, verbose_name="班组状态", null=True, blank=True, help_text="班组状态")
    parent = models.ForeignKey(
        to="Dept",
        on_delete=models.CASCADE,
        default=None,
        verbose_name="上级班组",
        db_constraint=False,
        null=True,
        blank=True,
        help_text="上级班组",
    )

    class Meta:
        db_table = "system_dept"
        verbose_name = "班组表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return self.name


class Workshop(models.Model):
    name = models.CharField(max_length=64, verbose_name="车间名称", help_text="车间名称")
    sort = models.IntegerField(default=1, verbose_name="显示排序", help_text="显示排序")
    owner = models.CharField(max_length=32, verbose_name="负责人", null=True, blank=True, help_text="负责人")
    phone = models.CharField(max_length=32, verbose_name="联系电话", null=True, blank=True, help_text="联系电话")
    email = models.EmailField(max_length=32, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")
    status = models.BooleanField(default=True, verbose_name="车间状态", null=True, blank=True, help_text="车间状态")
    parent = models.ForeignKey(
        to="Workshop",
        on_delete=models.CASCADE,
        default=None,
        verbose_name="上级车间",
        db_constraint=False,
        null=True,
        blank=True,
        help_text="上级车间",
    )

    class Meta:
        db_table = "system_workshop"
        verbose_name = "车间表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return self.name

class Railway_sections(models.Model):
    name = models.CharField(max_length=64, verbose_name="站段名称", help_text="站段名称")
    sort = models.IntegerField(default=1, verbose_name="显示排序", help_text="显示排序")
    owner = models.CharField(max_length=32, verbose_name="负责人", null=True, blank=True, help_text="负责人")
    phone = models.CharField(max_length=32, verbose_name="联系电话", null=True, blank=True, help_text="联系电话")
    email = models.EmailField(max_length=32, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")
    status = models.BooleanField(default=True, verbose_name="站段状态", null=True, blank=True, help_text="站段状态")
    parent = models.ForeignKey(
        to="Workshop",
        on_delete=models.CASCADE,
        default=None,
        verbose_name="上级站段",
        db_constraint=False,
        null=True,
        blank=True,
        help_text="上级站段",
    )

    class Meta:
        db_table = "system_railway_sections"
        verbose_name = "站段表"
        verbose_name_plural = verbose_name
        ordering = ("sort",)

    def __str__(self):
        return self.name




class VerifyCode(models.Model):
    """
    短信验证码，可以保存在redis等中
    """
    code = models.CharField(max_length=20, verbose_name='验证码', help_text='验证码')
    mobile = models.CharField(max_length=11, verbose_name='电话', help_text='电话')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        db_table = "table_verifycode"
        verbose_name_plural = verbose_name = '短信验证码'
        # ordering = ("-create_datetime",)

    def __str__(self):
        return self.code