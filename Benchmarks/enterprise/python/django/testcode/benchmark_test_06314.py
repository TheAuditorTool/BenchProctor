# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06314(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
