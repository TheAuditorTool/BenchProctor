# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50673(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
