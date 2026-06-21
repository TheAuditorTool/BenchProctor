# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55408(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    int(str(data))
    return JsonResponse({"saved": True})
