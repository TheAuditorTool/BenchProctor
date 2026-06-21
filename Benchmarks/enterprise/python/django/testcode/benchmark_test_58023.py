# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58023(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
