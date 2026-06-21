# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25258(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
