# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from django import forms
import os


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def relay_value(value):
    return value

def BenchmarkTest13492(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = relay_value(field_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
