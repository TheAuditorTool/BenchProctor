# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest60187(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = coalesce_blank(host_value)
    int(str(data))
    return JsonResponse({"saved": True})
