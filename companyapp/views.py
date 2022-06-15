from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Company, Category, Comment

#  Home Page
def HomePage(request):
    first_companies = Company.objects.first()
    three_companies = Company.objects.all()[1:4]
    three_categories = Category.objects.all()[0:3]

    return render(request, 'home.html', {
        'first_companies': first_companies,
        'three_companies': three_companies,
        'three_categories': three_categories,
    })


# All Companies Page
def all_companies(request):
    all_companies = Company.objects.all()
    return render(request, 'all-companies.html', {
        'all_companies': all_companies
    })


# Deatil Page
def detail(request, id):
    company = Company.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['message']
        Comment.objects.create(
            company=company,
            name=name,
            email=email,
            comment=comment,
        )
        messages.success(request, 'comment submitted but in moderation mode.')
    category = Category.objects.get(id=company.category.id)
    rel_company = Company.objects.filter(category=category).exclude(id=id)
    comments = Comment.objects.filter(company=company, status=True).order_by('-id')
    return render(request, 'company-detail.html', {
        'company': company,
        'related_company': rel_company,
        'comments': comments
    })


# fetch all category
def all_category(request):
    cats = Category.objects.all()
    return render(request, 'category.html', {
        'cats': cats
    })


# fetch companies in category
def category(request, id):
    category = Category.objects.get(id=id)
    companies = Company.objects.filter(category=category)
    return render(request, 'category-companies.html', {
        'all_companies': companies,
        'category': category
    })