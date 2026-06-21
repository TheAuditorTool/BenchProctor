# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53850(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
