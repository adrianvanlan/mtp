from django.db import models

TIPOS_NODO = (("L", "Localidad"), ("F", "Estación ferrocarril"), ("A", "Aeropuerto"), ("S", "Silos"), ("P", "Puerto"))

class Nodo(models.Model):

	nombre = models.CharField(max_length=50)
	latitud = models.CharField(max_length=20)
	longitud = models.CharField(max_length=20)
	tipo = models.CharField(max_length=1, choices=TIPOS_NODO)

	class Meta:
		verbose_name = "Nodo"
		verbose_name_plural = "Nodos"


	def __str__(self):
		pass


class Arco(models.Model):

	nodo_desde = models.ForeignKey('Nodo', null=False, related_name='nodo_desde')
	nodo_hasta = models.ForeignKey('Nodo', null=False, related_name='nodo_hasta')
	costo = models.PositiveIntegerField(null=False, blank=False)
	precio = models.Float(null=False, blank=False)
	tiempo = models.P
	
	class Meta:
		verbose_name = "Arco"
		verbose_name_plural = "Arcos"

	def __str__(self):
		pass