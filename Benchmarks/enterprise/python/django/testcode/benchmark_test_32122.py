# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32122(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
