# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest03104(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    exec(str(data))
    return JsonResponse({"saved": True})
