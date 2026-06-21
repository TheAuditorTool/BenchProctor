# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35478(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
