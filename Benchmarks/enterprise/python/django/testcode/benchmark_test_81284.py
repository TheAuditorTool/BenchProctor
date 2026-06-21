# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81284(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
