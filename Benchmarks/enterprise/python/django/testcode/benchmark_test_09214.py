# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09214(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = header_value if header_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
