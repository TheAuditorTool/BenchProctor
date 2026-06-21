# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37377(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
