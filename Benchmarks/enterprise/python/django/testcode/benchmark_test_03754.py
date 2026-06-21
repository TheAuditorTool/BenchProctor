# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03754(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    eval(str(data))
    return JsonResponse({"saved": True})
