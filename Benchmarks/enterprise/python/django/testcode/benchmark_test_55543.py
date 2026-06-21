# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55543(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
