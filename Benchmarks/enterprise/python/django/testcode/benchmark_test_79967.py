# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79967(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
