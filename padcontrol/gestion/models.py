from django.db import models


class Analistas(models.Model):
    nombre = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Analista"
        verbose_name_plural = "Analistas"
        managed = True
        db_table = 'analistas'

    def __str__(self):
        return f'{self.nombre}'


class Dependencias(models.Model):
    clave = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    inicio_ciclo = models.DateField(blank=True, null=True, verbose_name="Inicio del ciclo")
    fin_ciclo = models.DateField(blank=True, null=True, verbose_name="Fin del ciclo")
    n_docentes = models.IntegerField(blank=True, null=True)
    id_analista = models.ForeignKey(Analistas, on_delete=models.PROTECT, db_column='id_analista', blank=True, null=True)

    class Meta:
        verbose_name = "Dependencia"
        verbose_name_plural = "Dependencias"
        managed = True
        db_table = 'dependencias'

    def __str__(self):
        return f'{self.clave} - {self.nombre}'


class Oficios(models.Model):
    n_oficio = models.CharField(unique=True, max_length=25)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    clave_depe = models.ForeignKey(Dependencias, on_delete=models.PROTECT, db_column='clave_depe', blank=True, null=True)
    n_pads = models.PositiveIntegerField()
    alcance = models.ForeignKey('self', on_delete=models.PROTECT, db_column='alcance', default='Envío único',
                                blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    altas = models.PositiveIntegerField(blank=False, null=False, default=0)
    bajas = models.PositiveIntegerField(blank=False, null=False, default=0)
    sustituciones = models.PositiveIntegerField(blank=False, null=False, default=0)
    pendientes = models.PositiveIntegerField(blank=False, null=False,default=0)

    class Meta:
        verbose_name = "Oficio"
        verbose_name_plural = "Oficios"
        managed = True
        db_table = 'oficios'

    def __str__(self):
        return f'Oficio No.{self.n_oficio} de {self.clave_depe} con {self.n_pads} reportes'

# class Envios(models.Model):
#    id_oficio = models.OneToOneField(Oficios, on_delete=models.PROTECT, db_column='id_oficio', primary_key=True)


#    class Meta:
#        verbose_name = "Envio"
#        verbose_name_plural = "Envios"
#        managed = True
#        db_table = 'envios'
#        unique_together = (('id_oficio', 'clave_depe'),)

#   def __str__(self):
#      return f'No. Oficio {self.id_oficio} Dependencia {self.clave_depe}'

# class EnvioOficio(models.Model):
#    Numoficio = models.CharField(Oficios, on_delete=models.CASCADE,db_column='Numoficio', unique=True)
#    clave_depenvio = models.ForeignKey(Dependencias, on_delete=models.CASCADE, db_column='clave_depenvio')
#    altas = models.PositiveIntegerField(blank=True, null=True)
#    bajas = models.PositiveIntegerField(blank = True, null= True)
#    sustituciones = models.PositiveIntegerField(blank= True, null= True)
#    pendientes = models.PositiveIntegerField(blank = True, null= True)
