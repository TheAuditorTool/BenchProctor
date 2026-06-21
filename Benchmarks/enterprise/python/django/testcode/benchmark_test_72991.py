# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest72991(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
