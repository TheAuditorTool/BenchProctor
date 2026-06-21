# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03947(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
