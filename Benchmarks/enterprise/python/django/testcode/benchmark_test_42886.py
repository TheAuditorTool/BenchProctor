# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42886(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % (referer_value,)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
