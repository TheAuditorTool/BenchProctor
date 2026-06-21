# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest19152(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
