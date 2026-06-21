# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03749(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
