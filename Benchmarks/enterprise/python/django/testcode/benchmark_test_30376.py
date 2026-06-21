# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30376(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
