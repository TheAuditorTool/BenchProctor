# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68371(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
