# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15290(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
