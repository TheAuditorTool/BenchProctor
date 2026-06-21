# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51837(request):
    raw_body = request.body.decode('utf-8')
    result = 100 / int(str(raw_body))
    return JsonResponse({"saved": True})
