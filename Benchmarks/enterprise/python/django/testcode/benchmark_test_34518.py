# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34518(request):
    raw_body = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    eval(str(data))
    return JsonResponse({"saved": True})
