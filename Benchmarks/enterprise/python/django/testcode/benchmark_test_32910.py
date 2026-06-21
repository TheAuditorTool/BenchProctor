# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32910(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
