# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
from app_runtime import db, User


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest52301(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    db.session.query(User).filter(User.id == data).all()
    return JsonResponse({"saved": True})
