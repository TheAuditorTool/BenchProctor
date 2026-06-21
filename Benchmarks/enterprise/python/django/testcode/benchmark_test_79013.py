# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79013(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
