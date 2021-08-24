from django.db import models

# Create your models here.
class Network(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    network = models.ForeignKey(Network, related_name="show", on_delete = models.CASCADE)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title





