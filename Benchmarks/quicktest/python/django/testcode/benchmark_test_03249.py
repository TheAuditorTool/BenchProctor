# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03249(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
