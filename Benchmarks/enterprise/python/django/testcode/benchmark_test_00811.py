# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00811(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
