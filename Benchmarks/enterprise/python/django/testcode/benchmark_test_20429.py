# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20429(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    int(str(data))
    return JsonResponse({"saved": True})
