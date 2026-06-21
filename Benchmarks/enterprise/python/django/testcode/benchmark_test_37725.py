# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import pickle


def BenchmarkTest37725(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
