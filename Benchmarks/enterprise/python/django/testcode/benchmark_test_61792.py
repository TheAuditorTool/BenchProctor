# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest61792(request):
    field_value = UserForm(request.POST).data.get('field', '')
    if field_value not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = field_value
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
