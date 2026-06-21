# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest55988(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = '%s' % str(field_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
