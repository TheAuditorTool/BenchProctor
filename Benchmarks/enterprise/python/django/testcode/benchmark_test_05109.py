# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest05109(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = handle(field_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
