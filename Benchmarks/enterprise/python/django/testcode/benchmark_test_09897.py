# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09897(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    int(str(data))
    return JsonResponse({"saved": True})
