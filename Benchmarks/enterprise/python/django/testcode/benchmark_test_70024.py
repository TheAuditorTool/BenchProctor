# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django import forms
from django.http import HttpResponse
import os
from types import SimpleNamespace


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest70024(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    return JsonResponse({"saved": True})
