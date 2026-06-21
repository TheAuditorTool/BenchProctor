# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53481(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = bytearray(int(origin_value) if str(origin_value).isdigit() else 0)
    return JsonResponse({"saved": True})
