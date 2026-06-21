# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09668(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
