# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00380(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    int(str(data))
    return JsonResponse({"saved": True})
