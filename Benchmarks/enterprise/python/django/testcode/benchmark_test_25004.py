# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25004(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
