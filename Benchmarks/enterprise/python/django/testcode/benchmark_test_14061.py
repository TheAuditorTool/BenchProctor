# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest14061(request):
    raw_body = request.body.decode('utf-8')
    data = ensure_str(raw_body)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
