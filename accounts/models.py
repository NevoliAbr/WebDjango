from django.db import models

class Moto(models.Model):
    modelo = models.TextField()
    propietario = models.TextField()
    descripcion = models.TextField()
    
    # Campo de texto libre para la persona asignada
    asignado = models.TextField()

    fecha_inicio_trabajo = models.DateField()

    precio_mano_obra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_accesorios = models.DecimalField(max_digits=10, decimal_places=2)
    pago_inicial = models.DecimalField(max_digits=10, decimal_places=2)

    imagen = models.ImageField(upload_to='motos/')

    activo = models.BooleanField(default=True) # Nuevo campo

    def __str__(self):
        return f"{self.modelo} - {self.propietario}"
