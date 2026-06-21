# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django import forms
from django.template import Template, Context


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def ensure_str(value):
    return str(value)

def BenchmarkTest39087(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ensure_str(field_value)
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
