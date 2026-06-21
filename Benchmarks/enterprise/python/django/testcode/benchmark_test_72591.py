# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72591(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value:
        data = header_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
