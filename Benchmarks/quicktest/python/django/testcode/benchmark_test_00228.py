# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00228(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
