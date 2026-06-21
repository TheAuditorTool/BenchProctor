# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest62667(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
