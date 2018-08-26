from django.db import models


class Departamento(models.Model):

    id = models.AutoField(
        primary_key=True,
        blank=False, null=False
    )
    nombre = models.CharField(
        max_length=20,
        blank=False, null=False)

    def __str__(self):
        return str(self.nombre)

    def __unicode__(self):
        return str(self.nombre)
