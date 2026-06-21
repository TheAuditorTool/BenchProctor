# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61799(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
