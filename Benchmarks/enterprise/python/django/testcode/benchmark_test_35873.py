# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35873(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
