from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return HttpResponse("<h1>Home Page</h1>")

def shop(response):
    return HttpResponse("<h1>Shop Page</h1>")

def orders(response):
    return HttpResponse("<h1>Order List</h1>")