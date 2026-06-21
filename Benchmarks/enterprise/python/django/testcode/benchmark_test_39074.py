# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import pickle


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest39074(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
