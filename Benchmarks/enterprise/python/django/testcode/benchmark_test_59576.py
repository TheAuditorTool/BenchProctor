# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59576(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    exec(str(data))
    return JsonResponse({"saved": True})
