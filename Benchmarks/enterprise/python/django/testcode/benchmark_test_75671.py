# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75671(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
