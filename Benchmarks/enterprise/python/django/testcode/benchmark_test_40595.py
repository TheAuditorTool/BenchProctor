# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest40595(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
