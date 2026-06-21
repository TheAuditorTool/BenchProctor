# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12119(request):
    raw_body = request.body.decode('utf-8')
    eval(str(raw_body))
    return JsonResponse({"saved": True})
