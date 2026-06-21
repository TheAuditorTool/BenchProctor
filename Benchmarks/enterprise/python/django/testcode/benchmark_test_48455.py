# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48455(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
