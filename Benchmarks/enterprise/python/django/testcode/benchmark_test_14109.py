# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14109(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    eval(str(data))
    return JsonResponse({"saved": True})
