# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest72390(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
