# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64519(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
