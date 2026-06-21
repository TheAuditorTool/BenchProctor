# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03761(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = default_blank(field_value)
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': data})))
