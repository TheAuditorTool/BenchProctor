# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49986(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
