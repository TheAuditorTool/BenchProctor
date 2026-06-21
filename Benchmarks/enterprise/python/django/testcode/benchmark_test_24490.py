# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24490(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
