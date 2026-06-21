# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40798(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ' '.join(str(header_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
