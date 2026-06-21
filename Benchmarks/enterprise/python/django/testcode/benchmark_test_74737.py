# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74737(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    exec(str(data))
    return JsonResponse({"saved": True})
