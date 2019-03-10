from django.shortcuts import render, get_object_or_404
from .models import *


# Class Based Views (CBVs) и использование Миксинов
class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
