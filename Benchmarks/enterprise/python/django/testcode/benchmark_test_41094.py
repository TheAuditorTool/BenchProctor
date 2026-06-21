# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41094(request):
    raw_body = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
