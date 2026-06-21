# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest09991(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
