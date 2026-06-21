# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18113(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
