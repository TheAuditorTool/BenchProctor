# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76413(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
