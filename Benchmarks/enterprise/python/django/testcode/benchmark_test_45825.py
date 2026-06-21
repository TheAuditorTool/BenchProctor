# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest45825(request):
    field_value = UserForm(request.POST).data.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
