# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22623(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = (lambda v: v.strip())(header_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
