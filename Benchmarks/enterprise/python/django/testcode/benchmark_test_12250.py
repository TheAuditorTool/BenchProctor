# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest12250(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    os.setuid(int(str(json_value)) if str(json_value).isdigit() else 0)
    return JsonResponse({"saved": True})
