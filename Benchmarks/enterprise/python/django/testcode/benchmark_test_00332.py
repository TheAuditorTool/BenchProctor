# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest00332(request):
    field_value = UserForm(request.POST).data.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
