# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61614(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    eval(str(data))
    return JsonResponse({"saved": True})
