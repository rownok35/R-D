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

    pubs = Publication.objects.filter(publishing_year = year).order_by('-cited_by')

    

     #Pagination
    showing_product = 50
    paginator = Paginator(pubs, showing_product)
    page = request.GET.get('page')

    try:
        page_product = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_product = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_product = paginator.page(page)
    
    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 10)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    # page_product = paginator.get_page(page)

    year = int(year)

    total_pubs = len(pubs)
    showing_items = len(page_product)

    context = { 'message': 'Hello, World! :)', 'years': years,'years_r':years_r, "types": types, "pubs": page_product, 'custom_range': custom_range, 'year_sidebar': year, "total_pubs": total_pubs, "showing_items": showing_items}
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

    pubs = Publication.objects.filter(document_type = document_type).order_by('-publishing_year','-cited_by')

    #Pagination
    showing_product = 50
    paginator = Paginator(pubs, showing_product)
    page = request.GET.get('page')

    try:
        page_product = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_product = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_product = paginator.page(page)
    
    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 10)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    # page_product = paginator.get_page(page)
    total_pubs = len(pubs)
    showing_items = len(page_product)

    context = { 'message': 'Hello, World! :)', 'years': years,'years_r':years_r, "types": types, "pubs": page_product, 'custom_range': custom_range, "total_pubs": total_pubs, "showing_items": showing_items}
    return render(request, 'publications/year.html', context)


def search(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    types = ["Conference Paper", "Article", "Book Chapter", "Book", "Editorial", "Review", "Letter"]
    years = list(year_publications.objects.all().values_list('year', flat=True))

    years_r = years.copy()
    years_r.sort(reverse=True)

    if search_query == '':
        pubs = []
    elif search_query == ',':
        pubs = []
    else:
        pubs = Publication.objects.filter(Q(document_type__icontains = search_query)| Q(authors__icontains = search_query) | Q(title__icontains = search_query) | Q(publishing_year__icontains = search_query))
    
    showing_results = len(pubs)

    #Pagination
    # showing_product = 7
    # paginator = Paginator(pubs, showing_product)
    # page = request.GET.get('page')

    # try:
    #     page_product = paginator.page(page)
    # except PageNotAnInteger:
    #     page = 1
    #     page_product = paginator.page(page)
    # except EmptyPage:
    #     page = paginator.num_pages
    #     page_product = paginator.page(page)
    
    # leftIndex = (int(page) - 4)

    # if leftIndex < 1:
    #     leftIndex = 1

    # rightIndex = (int(page) + 5)

    # if rightIndex > paginator.num_pages:
    #     rightIndex = paginator.num_pages + 1

    # custom_range = range(leftIndex, rightIndex)


    # page_product = paginator.get_page(page)

    context = {
                'years': years,'years_r':years_r, 
                "types": types, 
                "pubs": pubs,
                "showing_results": showing_results,
                # 'custom_range': custom_range,

                }
    return render(request, 'publications/search.html', context)