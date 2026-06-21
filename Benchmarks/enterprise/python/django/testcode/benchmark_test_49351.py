# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49351(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    size = min(int(auth_header) if str(auth_header).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
