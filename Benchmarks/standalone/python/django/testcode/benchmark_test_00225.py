# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00225(request):
    field_value = request.POST.get('field', '')
    form = FormData(payload=field_value)
    data = form.payload
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
