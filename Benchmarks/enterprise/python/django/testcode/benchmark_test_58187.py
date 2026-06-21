# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest58187(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
