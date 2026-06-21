# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14602(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
