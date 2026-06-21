# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40142(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
