# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24790(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
