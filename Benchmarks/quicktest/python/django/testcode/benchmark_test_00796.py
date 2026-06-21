# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def relay_value(value):
    return value

def BenchmarkTest00796(request):
    raw_body = request.body.decode('utf-8')
    data = relay_value(raw_body)
    os.seteuid(65534)
    return JsonResponse({"saved": True})
