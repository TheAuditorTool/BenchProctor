# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms
from django.http import HttpResponse


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def relay_value(value):
    return value

def BenchmarkTest52216(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = relay_value(field_value)
    def _primary():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
