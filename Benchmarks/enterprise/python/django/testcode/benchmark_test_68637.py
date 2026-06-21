# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68637(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
