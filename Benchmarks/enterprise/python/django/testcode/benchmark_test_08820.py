# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08820(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
