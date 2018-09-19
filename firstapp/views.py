from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return HttpResponse("<h2>Hello World!</h2>")

def about(request):
    return HttpResponse("Page about it")

def product(request, productid):
    category = request.GET.get("cat", "")
    output = 'Page contact # {0}, category {1}'.format(productid, category)
    return HttpResponse(output)

def user_my(request, name="Tom", age=23):
    output = "User: {0}, age: {1}".format(name, age)
    return HttpResponse(output)
def contact(request):
    return HttpResponseRedirect('/user_my')

def temp(request):
    return render(request, 'firstapp/index.html')