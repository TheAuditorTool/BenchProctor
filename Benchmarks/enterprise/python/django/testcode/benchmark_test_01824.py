# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01824(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    int(str(data))
    return JsonResponse({"saved": True})
