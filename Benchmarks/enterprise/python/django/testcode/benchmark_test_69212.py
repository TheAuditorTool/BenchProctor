# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69212(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
