# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest71232(request):
    field_value = UserForm(request.POST).data.get('field', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
