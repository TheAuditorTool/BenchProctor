# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29312(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
