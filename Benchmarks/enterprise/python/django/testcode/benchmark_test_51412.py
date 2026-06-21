# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51412(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
