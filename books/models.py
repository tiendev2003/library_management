from django.db import models

class AuthGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'custom_auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        db_table = 'custom_auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'custom_auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'custom_auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'custom_auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'custom_auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'custom_django_admin_log'


class DjangoContentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'custom_django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    session_key = models.CharField(max_length=40, unique=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'custom_django_session'

class Books(models.Model):
    id_sach = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    id_category = models.ForeignKey('Categories', on_delete=models.CASCADE, db_column='id_category')
    ngay_tao = models.CharField(max_length=50)

    class Meta:
        db_table = 'books'


class Categories(models.Model):
    id_category = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'categories'


class Ctkiemkes(models.Model):
    id_ctkiemke = models.CharField(primary_key=True, max_length=100)
    id_kiemke = models.ForeignKey('Kiemkes', on_delete=models.CASCADE, db_column='id_kiemke')
    id_sach = models.ForeignKey(Books, on_delete=models.CASCADE, db_column='id_sach')
    so_luong_kiemke = models.IntegerField()
    so_luong_bandau = models.IntegerField()

    class Meta:
        db_table = 'ctkiemkes'


class Ctphieuhuys(models.Model):
    id_ctphieuhuy = models.CharField(primary_key=True, max_length=100)
    id_phieuhuy = models.ForeignKey('Phieuhuys', on_delete=models.CASCADE, db_column='id_phieuhuy')
    id_sach = models.ForeignKey(Books, on_delete=models.CASCADE, db_column='id_sach')
    so_luong = models.IntegerField()
    ly_do_huy = models.CharField(max_length=500)

    class Meta:
        db_table = 'ctphieuhuys'


class Ctphieunhaps(models.Model):
    id_ctphieunhap = models.CharField(primary_key=True, max_length=100)
    id_phieunhap = models.ForeignKey('Phieunhaps', on_delete=models.CASCADE, db_column='id_phieunhap')
    id_sach = models.ForeignKey(Books, on_delete=models.CASCADE, db_column='id_sach')
    so_luong = models.IntegerField()
    gia_nhap = models.FloatField()

    class Meta:
        db_table = 'ctphieunhaps'



class Docgias(models.Model):
    id_docgia = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    gender = models.IntegerField()
    birthday = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    ngay_tao = models.CharField(max_length=50)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'docgias'


class Kiemkes(models.Model):
    id_kiemke = models.CharField(primary_key=True, max_length=100)
    ngay_tao = models.CharField(max_length=50)
    ly_do = models.CharField(max_length=255)
    file_kiemke = models.CharField(max_length=255)
    id_user = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='id_user')

    class Meta:
        db_table = 'kiemkes'


class Phieuhuys(models.Model):
    id_phieuhuy = models.CharField(primary_key=True, max_length=100)
    ngay_huy = models.CharField(max_length=50)
    is_delete = models.BooleanField(default=False)
    id_user = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='id_user')

    class Meta:
        db_table = 'phieuhuys'


class Phieumuons(models.Model):
    id_phieumuon = models.CharField(primary_key=True, max_length=100)
    ngay_tao = models.CharField(max_length=50)
    ngay_hen_tra = models.CharField(max_length=50)
    trang_thai = models.IntegerField()
    ngay_tra = models.CharField(max_length=50)
    ghi_chu = models.CharField(max_length=255)
    so_luong = models.IntegerField()
    id_user = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='id_user')
    id_sach = models.ForeignKey(Books, on_delete=models.CASCADE, db_column='id_sach')
    id_the = models.ForeignKey('Thethuviens', on_delete=models.CASCADE, db_column='id_the')
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'phieumuons'


class Phieunhaps(models.Model):
    id_phieunhap = models.CharField(primary_key=True, max_length=100)
    donvi_cungcap = models.CharField(max_length=255)
    ngay_nhap = models.CharField(max_length=50)
    ly_do_nhap = models.CharField(max_length=255)
    id_user = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='id_user')
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'phieunhaps'


class Thethuviens(models.Model):
    id_the = models.CharField(primary_key=True, max_length=100)
    type = models.IntegerField()
    ngay_tao = models.CharField(max_length=50)
    ngay_het_han = models.CharField(max_length=50)
    ghi_chu = models.CharField(max_length=255)
    id_docgia = models.ForeignKey(Docgias, on_delete=models.CASCADE, db_column='id_docgia')
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'thethuviens'


class Users(models.Model):
    id_user = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.IntegerField()
    gender = models.IntegerField()
    birthday = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
        
class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    purchase_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name