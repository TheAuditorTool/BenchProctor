# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20187(request):
    raw_body = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    int(str(data))
    return JsonResponse({"saved": True})
