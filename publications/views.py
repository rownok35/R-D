from django.shortcuts import render
from django.http import HttpResponse
from .models import year_publications, Publication
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def home(request):

    types = ["Conference Paper", "Article", "Book Chapter", "Book", "Editorial", "Review", "Letter"]
    years = list(year_publications.objects.all().values_list('year', flat=True))

    years_r = years.copy()
    years_r.sort(reverse=True)

    publication_number = list(year_publications.objects.all().values_list('publication_number', flat=True)) 

    context = { 'message': 'Hello, World! :)', 'years': years, 'publication_number': publication_number, 'years_r':years_r, "types": types}

    return render(request, 'publications/home.html', context)


def year_wise_publications(request, year):
    # print("year ",year)
    types = ["Conference Paper", "Article", "Book Chapter", "Book", "Editorial", "Review", "Letter"]
    years = list(year_publications.objects.all().values_list('year', flat=True))

    years_r = years.copy()
    years_r.sort(reverse=True)

    pubs = Publication.objects.filter(publishing_year = year)

    #Pagination
    showing_product = 7
    paginator = Paginator(pubs, showing_product)
    page = request.GET.get('page')
    page_product = paginator.get_page(page)

    context = { 'message': 'Hello, World! :)', 'years': years,'years_r':years_r, "types": types, "pubs": page_product}
    return render(request, 'publications/year.html', context)


def details(request, id):
    types = ["Conference Paper", "Article", "Book Chapter", "Book", "Editorial", "Review", "Letter"]
    years = list(year_publications.objects.all().values_list('year', flat=True))

    years_r = years.copy()
    years_r.sort(reverse=True)

    pub = Publication.objects.get(id = id)


    context = { 'message': 'Hello, World! :)', 'years': years,'years_r':years_r, "types": types, "pub": pub}
    return render(request, 'publications/details.html', context)


def category(request, document_type):

   
    types = ["Conference Paper", "Article", "Book Chapter", "Book", "Editorial", "Review", "Letter"]
    years = list(year_publications.objects.all().values_list('year', flat=True))

    years_r = years.copy()
    years_r.sort(reverse=True)

    pubs = Publication.objects.filter(document_type = document_type)

    #Pagination
    showing_product = 7
    paginator = Paginator(pubs, showing_product)
    page = request.GET.get('page')
    page_product = paginator.get_page(page)

    context = { 'message': 'Hello, World! :)', 'years': years,'years_r':years_r, "types": types, "pubs": page_product}
    return render(request, 'publications/year.html', context)


def search(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    types = ["Conference Paper", "Article", "Book Chapter", "Book", "Editorial", "Review", "Letter"]
    years = list(year_publications.objects.all().values_list('year', flat=True))

    years_r = years.copy()
    years_r.sort(reverse=True)

    pubs = Publication.objects.filter(Q(document_type__icontains = search_query)| Q(authors__icontains = search_query) | Q(title__icontains = search_query) | Q(publishing_year__icontains = search_query))

    #Pagination
    showing_product = 7
    paginator = Paginator(pubs, showing_product)
    page = request.GET.get('page')
    page_product = paginator.get_page(page)

    context = { 'message': 'Hello, World! :)', 'years': years,'years_r':years_r, "types": types, "pubs": page_product}
    return render(request, 'publications/year.html', context)
