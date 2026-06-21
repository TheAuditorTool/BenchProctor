# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import re
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest53976(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
