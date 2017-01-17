from __future__ import unicode_literals
from django.db import models

class Razones_Sociales(models.Model):
    RAZON_CHOICES=(
        ('grupo tenis show sa de cv', 'GRUPO TENIS SHOW SA DE CV'),
        ('elia daissa monarrez','ELIA DAISSA MONARREZ'),
        ('elia denisse monarrez','ELIA DENISSE MONARREZ'),
        ('hector ernesto monarrez palazuelos','HECTOR ERNESTO MONARREZ PALAZUELOS')
    )
    razon=models.CharField(max_length=50,choices=RAZON_CHOICES)
    rfc=models.CharField(max_length=50)

class Sucursales(models.Model):
    PLAZA_CHOICES=(
        ('san isidro','San Isidro'),
        ('walmart','Walmart'),
        ('forum','Forum'),
        ('galerias san miguel','Galerias San Miguel'),
        ('plaza fiesta','Plaza Fiesta'),
        ('puerto paraiso','Puerto Paraiso'),
        ('las plazas','Las Plazas Outlet'),
        ('outlet mulza','Outlet Mulza'),
        ('oficina','Oficina Mara')
    )
    MARCA_CHOICES=(
        ('lacoste','Lacoste'),
        ('the body shop','The Body Shop'),
        ('benissimo','Benissimo'),
        ('tenis show','Tenis Show'),
        ('kenneth cole','Kenneth Cole')
    )
    CIUDAD_CHOICES=(
        ('culiacan','Culiacan'),
        ('leon','Leon'),
        ('guadalajara','Guadalajara'),
        ('cabo san lucas','Cabo San Lucas')
    )
    marca=models.CharField(max_length=80,choices=MARCA_CHOICES)
    ciudad=models.CharField(max_length=80,choices=CIUDAD_CHOICES)
    plaza=models.CharField(max_length=80,choices=PLAZA_CHOICES)
    telefono=models.CharField(max_length=20)
    correo=models.EmailField(max_length=249)
    domicilio=models.CharField(max_length=249)
    rs=models.ForeignKey(Razones_Sociales)
    def __str__(self):
        return '{} {} {}'.format(self.marca.capitalize(),self.plaza.capitalize(),self.ciudad.capitalize())

class Empleados(models.Model):
    SEX_CHOICES=(
        (0,'Mujer'),
        (1,'Hombre')
    )
    PUESTO_CHOICES=(
        ('recursos humanos','Recurso Humanos'),
        ('informatica','Informatica'),
        ('auxiliar de almacen','Auxiliar de almacen'),
        ('credito','Credito'),
        ('auxiliar administrativo','Auxiliar administrativo'),
        ('guardia','Guardia'),
        ('asesor','Asesor'),
        ('sublider','Sublider'),
        ('lider','Lider'),
        ('coordinar de operaciones','Coordinador de operaciones')
    )
    nombre=models.CharField(max_length=150)
    telefono=models.CharField(max_length=50)
    curp=models.CharField(max_length=50)
    imss=models.CharField(max_length=50)
    no_imss=models.CharField(max_length=50)
    bod=models.DateField(auto_now=False,auto_now_add=False)
    sexo=models.BooleanField(default=0)
    ingreso=models.DateField(auto_now=True)
    salida=models.DateField(auto_now_add=True)
    estado=models.BooleanField(default=1,choices=SEX_CHOICES)
    puesto=models.CharField(max_length=100,choices=PUESTO_CHOICES)
    sueldo=models.DecimalField(max_digits=10,decimal_places=2)
    direccion=models.CharField(max_length=249)
    infonavit=models.CharField(max_length=150)
    rfc=models.CharField(max_length=50)
    sucursal=models.ForeignKey(Sucursales)

    def __str__(self):
        return self.nombre
