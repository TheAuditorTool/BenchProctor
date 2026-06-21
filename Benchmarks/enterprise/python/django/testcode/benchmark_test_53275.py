# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os
import time


def coalesce_blank(value):
    return value or ''

def BenchmarkTest53275(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
