# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest66129(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ensure_str(json_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
