from django.shortcuts import render,redirect
from .models import Film,Category
from .forms import FilmCreate
# Create your views 


def Main(request):
    Films=Film.objects.all()
    category=Category.objects.all()

    context={
        'films': Films,
        'title': f'All Movies',
        'categories': category
    }
    return render(
        request=request,
        template_name='main/index.html',
        context=context
      
    )

def film_details(request, id):
    Films=Film.objects.get(id=id)
    category=Category.objects.all()

    context={
        'film':Films,
        'categories':category
    }
    return render(
        request=request,
        template_name='main/film_details.html',
        context=context
    )

def film_create(request):
    if not request.user.is_authenticated:
        return redirect('home')
    category=Category.objects.all()
    context={
        'form':FilmCreate,
        'title':'Uploading New Movie',
        'categories':category,
        'btn':"Create",
        'color':'primary'
    }
    if request.method=='POST':
        form=FilmCreate(request.POST,request.FILES)
        if form.is_valid():
            film = form.save(commit=False)
            film.owner=request.user
            film.save()
            return redirect('home')
    return render(
        request=request,
        template_name='main/film_create.html',
        context=context
    )

def search(request):
    q=request.GET.get('q', None)

    category=Category.objects.all()
    films=Film.objects.filter(title__icontains=q)
    context={
        'films':films,
        'categories':category,
        'title':f'Here is the movie you have searched'
    }


    return render(
        request=request,
        template_name='main/for_search.html',
        context=context
    )

def category(request, id):
    category_name=Category.objects.get(id=id).name
    print(category_name)
    films=Film.objects.filter(category__name=category_name)
    category=Category.objects.all()
  
    context={
        'films':films,
        'categories':category,
        'title':f'{category_name} movies'
    }
    return render(
        request=request,
        template_name='main/for_search.html',
        context=context
    )


def film_delate(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    film = Film.objects.filter(id=id)
    film.delete()
    return redirect('home')
 
def film_update(request, id):
    category=Category.objects.all()
    film=Film.objects.get(id=id)
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = FilmCreate(request.POST, request.FILES,instance=film)
        if form.is_valid():
            form.save()
            return redirect('home')




    form=FilmCreate(instance=film)
    context={
        'form':form,
        'categories':category,
        'title': f'Update {film.title}',
        'btn':'Update',
        'color':'success'
    }
    return render(
        request=request,
        template_name='main/film_create.html',
        context=context
    )


def profile(request):
    if not  request.user.is_authenticated:
        return redirect('login')

    film = Film.objects.filter(owner=request.user)
    print(film)
    category =Category.objects.all()
    context={
        'title':'My Movies',
        'films':film,
        'categories':category
    }

    return render(
        request=request,
        template_name='main/profile.html',
        context=context
    )