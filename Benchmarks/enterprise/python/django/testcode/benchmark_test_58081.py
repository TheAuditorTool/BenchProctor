# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)
def coalesce_blank(value):
    return value or ''

def BenchmarkTest58081(request):
    field_value = UserForm(request.POST).data.get('field', '')
    data = coalesce_blank(field_value)
    processed = data[:64]
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(processed)})
