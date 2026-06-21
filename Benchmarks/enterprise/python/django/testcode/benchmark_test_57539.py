# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57539(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
