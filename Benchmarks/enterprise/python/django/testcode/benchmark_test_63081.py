# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63081(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
