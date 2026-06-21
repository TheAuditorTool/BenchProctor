# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest80955(request):
    raw_body = request.body.decode('utf-8')
    os.remove(str(raw_body))
    return JsonResponse({"saved": True})
