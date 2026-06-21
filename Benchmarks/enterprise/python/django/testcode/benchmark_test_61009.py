# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61009(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    int(str(data))
    return JsonResponse({"saved": True})
