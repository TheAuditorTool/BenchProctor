# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65801(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
