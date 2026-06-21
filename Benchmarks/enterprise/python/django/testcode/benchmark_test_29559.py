# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29559(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
