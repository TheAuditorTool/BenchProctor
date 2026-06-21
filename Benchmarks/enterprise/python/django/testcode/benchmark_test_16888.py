# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest16888(request):
    field_value = UserForm(request.POST).data.get('field', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if field_value not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + field_value
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
