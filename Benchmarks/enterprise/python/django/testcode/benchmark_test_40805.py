# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40805(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
