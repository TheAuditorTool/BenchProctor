# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00522(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
