# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11911(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
