# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms
import os
import importlib


class UserForm(forms.Form):
    field = forms.CharField(required=False)
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest03176(request):
    field_value = UserForm(request.POST).data.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
