# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50727(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
