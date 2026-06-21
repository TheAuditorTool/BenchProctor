# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77990(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
