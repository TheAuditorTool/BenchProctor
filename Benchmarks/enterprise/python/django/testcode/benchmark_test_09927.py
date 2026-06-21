# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09927(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    eval(str(data))
    return JsonResponse({"saved": True})
