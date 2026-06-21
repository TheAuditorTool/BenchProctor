# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64779(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
