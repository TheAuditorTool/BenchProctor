# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest42301(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
