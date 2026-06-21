# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest11616(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
