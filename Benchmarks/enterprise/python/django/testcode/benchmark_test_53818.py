# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53818(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
