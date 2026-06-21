# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15840(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    eval(str(data))
    return JsonResponse({"saved": True})
