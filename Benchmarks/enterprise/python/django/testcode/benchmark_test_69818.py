# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69818(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
