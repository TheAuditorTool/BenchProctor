# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest24293(request):
    field_value = UserForm(request.POST).data.get('field', '')
    random.seed(int(field_value) if str(field_value).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
