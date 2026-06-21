# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django import forms


class UserForm(forms.Form):
    field = forms.CharField(required=False)

def BenchmarkTest03753(request):
    field_value = UserForm(request.POST).data.get('field', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(field_value).replace('\r', '').replace('\n', ''))
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
