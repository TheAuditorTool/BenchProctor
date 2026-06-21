# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46595(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
