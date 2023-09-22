from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    nombre = models.TextField(max_length=100)
    curp = models.TextField(max_length=19)
    id = models.BigAutoField(primary_key=True)

class Pollsters(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    grupo = models.CharField(max_length=10)
    unidadap = models.CharField(max_length=50)
    tuition = models.CharField(max_length=30)

class User_Pollsters(models.Model):
    STATUS = (
            ('Pendiente','Pendiente'),
            ('Aceptado','Aceptado'),
            )


    pollster = models.ForeignKey(Pollsters,null=False,on_delete=models.CASCADE)
    investigator = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,null=False)
    status = models.CharField(max_length=200,null=False,choices=STATUS)

    class cuestionario(models.Model):
        id = models.BigAutoField(primary_key=True)
        Infancia_y_Adolescencia = "IyA"
        Adultez = "A"
        Vejez = "V"
        Mujer_Embrazada = "ME"
        Identificacion_Opciones = [
            (Infancia_y_Adolescencia, 'Infancia y Adolescencia'),
            (Adultez, 'Adultez'),
            (Vejez, 'Vejez'),
            (Mujer_Embrazada, 'Mujer Embrazada'),
        ]
        identificacion = models.CharField(max_length=3, choices=Identificacion_Opciones,
                                          default=Infancia_y_Adolescencia)
        #Seccion socioecnómica
        #1. ¿Cuál es su nivel de escolaridad?
        #a) Ninguno
        #b) Primaria
        #c) Secundaria
        #d) Preparatoria
        #e) Licenciatura
        #f) Posgrado
        #g) No sabe
        Ninguno = "N"
        Primaria = "P"
        Secundaria = "S"
        Preparatoria = "PR"
        Licenciatura = "L"
        Posgrado = "PO"
        No_sabe = "NS"
        Nivel_Escolaridad_Opciones = [ (Ninguno, 'Ninguno'), (Primaria, 'Primaria'), (Secundaria, 'Secundaria'),
                                       (Preparatoria, 'Preparatoria'), (Licenciatura, 'Licenciatura'),
                                       (Posgrado, 'Posgrado'), (No_sabe, 'No sabe'), ]
        escolaridad = models.CharField(max_length=2, choices=Nivel_Escolaridad_Opciones, default=Ninguno)
        #2. ¿Cuál es su ocupación?
        #a) Trabajador del hogar
        #b) Estudiante
        #c) Jubilado
        #d) Desempleado
        #e) Trabajador
        #f) No sabe
        Trabajador_del_hogar = "TH"
        Estudiante = "E"
        Jubilado = "J"
        Desempleado = "D"
        Trabajador = "T"
        No_sabe = "NS"
        Ocupacion_Opciones = [ (Trabajador_del_hogar, 'Trabajador del hogar'), (Estudiante, 'Estudiante'),
                                 (Jubilado, 'Jubilado'), (Desempleado, 'Desempleado'), (Trabajador, 'Trabajador'),
                                 (No_sabe, 'No sabe'), ]
        ocupacion = models.CharField(max_length=2, choices=Ocupacion_Opciones, default=Trabajador_del_hogar)
        #3. ¿Cuál es el total de ingresos familiar?
        #a) Menos de 1 salario mínimo
        #b) Entre 1 y 2 salarios mínimos
        #c) Entre 2 y 3 salarios mínimos
        #d) Entre 3 y 4 salarios mínimos
        #e) Más de 4 salarios mínimos
        #f) No sabe
        Salario_minimo = "SM"
        Entre_1_y_2_salarios_minimos = "1-2SM"
        Entre_2_y_3_salarios_minimos = "2-3SM"
        Entre_3_y_4_salarios_minimos = "3-4SM"
        Mas_de_4_salarios_minimos = "4SM"
        No_sabe = "NS"
        Ingresos_Familiares_Opciones = [ (Salario_minimo, 'Menos de 1 salario mínimo'),
                                         (Entre_1_y_2_salarios_minimos, 'Entre 1 y 2 salarios mínimos'),
                                         (Entre_2_y_3_salarios_minimos, 'Entre 2 y 3 salarios mínimos'),
                                         (Entre_3_y_4_salarios_minimos, 'Entre 3 y 4 salarios mínimos'),
                                         (Mas_de_4_salarios_minimos, 'Más de 4 salarios mínimos'),
                                         (No_sabe, 'No sabe'), ]
        ingresos_familiares = models.CharField(max_length=5, choices=Ingresos_Familiares_Opciones,
                                               default=Salario_minimo)


