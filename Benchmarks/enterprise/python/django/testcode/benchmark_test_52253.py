# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52253(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
