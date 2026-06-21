# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66580(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
