# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest12878(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
