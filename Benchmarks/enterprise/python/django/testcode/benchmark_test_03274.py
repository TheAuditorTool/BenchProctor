# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django import forms
from django.template import Template, Context


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest03274(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
