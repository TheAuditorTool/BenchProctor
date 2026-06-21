# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24167(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    int(str(data))
    return JsonResponse({"saved": True})
