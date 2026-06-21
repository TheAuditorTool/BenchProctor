# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76696(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    prefix = ''
    data = prefix + str(header_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
