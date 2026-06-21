# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10237(request):
    raw_body = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
