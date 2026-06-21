# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80282(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    eval(str(data))
    return JsonResponse({"saved": True})
