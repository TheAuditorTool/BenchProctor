# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest15919(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
