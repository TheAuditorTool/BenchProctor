# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest56893(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '{}'.format(field_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
