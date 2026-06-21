# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05463(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
