# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56463(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value:
        data = header_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
