# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43459(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
