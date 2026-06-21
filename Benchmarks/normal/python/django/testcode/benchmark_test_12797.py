# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest12797(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
