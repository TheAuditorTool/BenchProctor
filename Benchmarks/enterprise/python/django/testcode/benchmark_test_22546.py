# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def relay_value(value):
    return value

def BenchmarkTest22546(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = relay_value(field_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
