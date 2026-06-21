# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22892(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    size = min(int(header_value) if str(header_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
