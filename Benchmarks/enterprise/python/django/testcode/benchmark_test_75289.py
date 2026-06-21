# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest75289(request):
    field_value = UserForm(request.POST).data.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
