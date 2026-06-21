# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19383(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
