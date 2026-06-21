# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60619(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
