# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import os
import importlib


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest40955(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = default_blank(field_value)
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
