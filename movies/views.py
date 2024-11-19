from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    movie_list = ['Gifted', 'The intern','Green Line']
    context = {
        'movie': movie_list
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})



#app/templates/app/index.html
#in our case : #movies/templates/movies/index.html

