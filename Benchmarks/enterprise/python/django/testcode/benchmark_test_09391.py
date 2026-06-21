# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09391(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
