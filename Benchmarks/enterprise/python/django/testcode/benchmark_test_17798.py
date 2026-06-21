# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17798(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
