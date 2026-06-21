# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest04190(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = unquote(field_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
