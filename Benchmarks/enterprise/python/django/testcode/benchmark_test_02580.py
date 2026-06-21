# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02580(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    eval(str(data))
    return JsonResponse({"saved": True})
