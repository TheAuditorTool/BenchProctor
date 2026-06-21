# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest12215(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = forwarded_ip
            data = parsed
        case _:
            data = forwarded_ip
    requests.get(str(data))
    return JsonResponse({"saved": True})
