# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09110(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
