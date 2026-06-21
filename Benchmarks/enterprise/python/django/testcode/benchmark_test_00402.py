# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00402(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
