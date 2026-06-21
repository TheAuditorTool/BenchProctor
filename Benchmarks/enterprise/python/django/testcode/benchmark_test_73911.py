# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73911(request):
    raw_body = request.body.decode('utf-8')
    request.session['data'] = str(raw_body)
    return JsonResponse({"saved": True})
