# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61438(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
