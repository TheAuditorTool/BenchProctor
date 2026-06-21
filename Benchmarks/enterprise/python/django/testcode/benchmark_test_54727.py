# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54727(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
