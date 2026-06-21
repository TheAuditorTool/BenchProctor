# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import pickle


def BenchmarkTest20295(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
