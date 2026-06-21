# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30668(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
