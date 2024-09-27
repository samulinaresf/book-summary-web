from django.shortcuts import render
from resumenes.models import Libro, Categoria, Autor
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
 
@login_required  
def mostrar_resumenes(request):
    libros = Libro.objects.filter()
    categorias = Categoria.objects.all()
    autores = Autor.objects.all()
    if not libros:
        print("No se encontraron libros en la base de datos.")
    else:
        print("Libros encontrados:", libros)
    paginator = Paginator(libros,2)
    page = request.GET.get('page')
    libros_paginados = paginator.get_page(page)
    libros_count = libros.count()
    context = {
        'libros':libros_paginados,
        'libros_count':libros_count,
        'categorias':categorias,
        'autores':autores
    }
    return render(request, 'resumenes.html',context)

"""def libros_por_categoria(request):
    libros = Libro.objects.all()
    libros_count = libros.count()
    categorias = Categoria.objects.all()
    if categorias:
        Libro.objects.filter()
    if not libros:
        print("No se encontraron libros en la base de datos.")
        libros_count = libros.count()
    else:
        print("Libros encontrados:", libros)
        libros_count = libros.count()
    context = {
        'libros':libros,
        'libros_count':libros_count,
        'categorias':categorias
        }
    return render(request, 'resumenes.html',context)

def libros_por_autor(request, slug_autor):
    libros = Libro.objects.filter(slug_autor=slug_autor)
    libros_count = libros.count()

    if not libros:
        print("No se encontraron libros en la base de datos.")
    else:
        print("Libros encontrados:", libros)
    context = {
            'libros':libros,
            'libros_count':libros_count
        }
    return render(request, 'resumenes.html',context)"""

def busqueda_producto(request):
    keyword = request.GET['keyword']
    libros = Libro.objects.none()  
    autor = Autor.objects.all()
    categorias = Categoria.objects.all()
    if keyword:
        libros = Libro.objects.filter(Q(titulo__icontains=keyword)|Q(id_autor__nombre__icontains=keyword)|Q(id_categoria__nombre__icontains=keyword)).order_by('titulo')
    print(f"Se han encontrado {libros.count()} libros")
    libros_count=libros.count()
    paginator = Paginator(libros, 2)
    page = request.GET.get('page')
    libros_paginados = paginator.get_page(page)
    context = {
        'libros':libros_paginados,
        'libros_count':libros_count,
        'autor':autor,
        'categorias':categorias
    }
    return render(request,'resumenes.html',context)