# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def ensure_str(value):
    return str(value)

def BenchmarkTest33075(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = ensure_str(field_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
