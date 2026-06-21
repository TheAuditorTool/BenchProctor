# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest62779(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
