# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00505(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request.session['data'] = str(ua_value)
    return JsonResponse({"saved": True})
