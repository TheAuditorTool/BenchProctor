# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest09453(request):
    raw_body = request.body.decode('utf-8')
    data = ensure_str(raw_body)
    os.seteuid(65534)
    return JsonResponse({"saved": True})
