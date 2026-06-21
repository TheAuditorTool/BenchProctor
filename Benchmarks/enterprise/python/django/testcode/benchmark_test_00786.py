# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from django import forms
import ast


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest00786(request):
    field_value = UserForm(request.POST).data.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    processed = data[:64]
    return HttpResponse(Template(processed).render(Context()))
