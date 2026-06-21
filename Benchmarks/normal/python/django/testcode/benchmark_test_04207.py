# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest04207(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        os.setuid(int(str(json_value)) if str(json_value).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
