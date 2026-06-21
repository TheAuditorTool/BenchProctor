# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52057(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
