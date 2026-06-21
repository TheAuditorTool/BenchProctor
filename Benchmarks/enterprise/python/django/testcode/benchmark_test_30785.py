# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30785(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
