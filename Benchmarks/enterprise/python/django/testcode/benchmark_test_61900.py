# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61900(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
