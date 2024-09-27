from django.db import models

# Creando los modelos

#Categorías de los libros
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        db_table = 'categoria'  
        managed = False

#Autores de los libros
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    class Meta:
        db_table = 'autor'              
        managed = False

#Libros
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    id_autor = models.ForeignKey(Autor, db_column="id_autor", on_delete=models.CASCADE,related_name="libros_por_autor")
    id_categoria = models.ForeignKey(Categoria, db_column="id_categoria", on_delete=models.CASCADE,related_name="libros_por_categoria")
    slug_autor = models.SlugField(max_length=100)
    slug_categoria = models.SlugField(max_length=100)
    
    fecha = models.IntegerField(default=20240815)
    valoracion = models.IntegerField(default=None)
    
    class Meta:
        db_table = 'libro'  
        managed = False
