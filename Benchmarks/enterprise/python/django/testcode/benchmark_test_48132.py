# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48132(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
