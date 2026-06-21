# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46377(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    eval(str(data))
    return JsonResponse({"saved": True})
