# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest36475(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
