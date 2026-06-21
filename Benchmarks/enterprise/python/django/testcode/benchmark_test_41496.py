# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41496(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
