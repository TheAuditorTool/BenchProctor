# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00114(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    exec(str(data))
    return JsonResponse({"saved": True})
