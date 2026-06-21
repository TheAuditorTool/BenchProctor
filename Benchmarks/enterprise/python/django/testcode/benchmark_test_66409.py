# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest66409(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
