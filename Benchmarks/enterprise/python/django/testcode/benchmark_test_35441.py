# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35441(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
