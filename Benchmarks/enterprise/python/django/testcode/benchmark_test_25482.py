# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import os
import importlib
import sys


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest25482(request):
    field_value = UserForm(request.POST).data.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
