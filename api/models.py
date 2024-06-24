from django.db import models
from .utils import delete_image


class LaboratoriosModel(models.Model):
    nombre_laboratorio = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Nombre del laboratorio"
    )
    imagen = models.ImageField(
        upload_to='laboratorios/',
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'Laboratorios'
        verbose_name = 'Laboratorio'
        verbose_name_plural = 'Laboratorios'

    def get_imagen_url(self, obj):
        if obj.imagen:
            return self.context['request'].build_absolute_uri(obj.imagen.url)
        return None

    def delete(self, using=None, keep_parents=False):
        delete_image(self)
        super().delete(using, keep_parents)

    def __str__(self):
        return self.nombre_laboratorio


class MarcasModel(models.Model):
    nombre_marca = models.CharField(
        max_length=55,
        unique=True,
        verbose_name="Nombre de la marca"
    )

    class Meta:
        db_table = 'Marcas'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nombre_marca


class TipoActivosModel(models.Model):
    nombre_tipo = models.CharField(
        max_length=55,
        unique=True,
        verbose_name="Nombre del equipo"
    )

    class Meta:
        db_table = 'TipoActivos'
        verbose_name = 'Tipo de Activo'
        verbose_name_plural = 'Tipos de Activos'

    def __str__(self):
        return self.nombre_tipo


class ActivosModel(models.Model):
    codigo_activo = models.CharField(
      max_length=12,
      unique=True,
      verbose_name="Código del activo"
    )
    laboratorio = models.ForeignKey(
        LaboratoriosModel,
        on_delete=models.CASCADE
    )
    tipo = models.ForeignKey(TipoActivosModel, on_delete=models.CASCADE)
    marca = models.ForeignKey(MarcasModel, on_delete=models.CASCADE)
    estado = models.CharField(
        max_length=15,
        choices=[
            ('OPERATIVO', 'OPERATIVO'),
            ('Mantenimiento', 'Mantenimiento'),
            ('BUEN ESTADO', 'BUEN ESTADO')
        ]
    )
    estado_uso = models.CharField(
        max_length=6,
        choices=[('NUEVO', 'Nuevo'), ('VIEJO', 'Viejo')]
    )
    observacion = models.TextField()
    imagen = models.ImageField(upload_to='activos/', blank=True, null=True)

    class Meta:
        db_table = 'Activos'
        verbose_name = 'Activo'
        verbose_name_plural = 'Activos'

    def get_imagen_url(self, obj):
        if obj.imagen:
            return self.context['request'].build_absolute_uri(obj.imagen.url)
        return None

    def delete(self, using=None, keep_parents=False):
        delete_image(self)
        super().delete(using, keep_parents)

    def __str__(self):
        return f"{self.codigo_activo} - {self.laboratorio}"
