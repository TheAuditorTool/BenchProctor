# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11327(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    eval(str(data))
    return JsonResponse({"saved": True})
