# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest75132(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    eval(str(data))
    return JsonResponse({"saved": True})
