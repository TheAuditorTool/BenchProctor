# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest00531(request):
    field_value = request.POST.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(field_value).strip()
        case _:
            data = str(field_value)
    requests.get(str(data))
    return JsonResponse({"saved": True})
