# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest52151(request):
    field_value = UserForm(request.POST).data.get('field', '')
    return JsonResponse({'error': str(field_value), 'stack': repr(locals())}, status=500)
