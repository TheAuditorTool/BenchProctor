# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01958(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    eval(str(data))
    return JsonResponse({"saved": True})
