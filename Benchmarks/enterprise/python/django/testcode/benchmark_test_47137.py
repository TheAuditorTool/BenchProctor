# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47137(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
