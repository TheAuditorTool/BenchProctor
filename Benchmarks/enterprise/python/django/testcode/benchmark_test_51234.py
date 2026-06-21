# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest51234(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
