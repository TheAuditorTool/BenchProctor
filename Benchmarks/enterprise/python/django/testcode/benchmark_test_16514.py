# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest16514(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
