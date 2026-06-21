# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68485(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    exec(str(data))
    return JsonResponse({"saved": True})
