# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40483(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
