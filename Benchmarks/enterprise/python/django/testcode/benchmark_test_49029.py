# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49029(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    int(str(data))
    return JsonResponse({"saved": True})
