# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59464(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
