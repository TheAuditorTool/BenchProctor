# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43796(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
