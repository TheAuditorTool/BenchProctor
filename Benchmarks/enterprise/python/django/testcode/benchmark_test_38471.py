# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest38471(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return JsonResponse({"saved": True})
