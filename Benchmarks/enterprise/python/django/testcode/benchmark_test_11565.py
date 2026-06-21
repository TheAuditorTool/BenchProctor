# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11565(request):
    host_value = request.META.get('HTTP_HOST', '')
    request.session.set_expiry(1800)
    request.session['data'] = str(host_value)
    return JsonResponse({"saved": True})
