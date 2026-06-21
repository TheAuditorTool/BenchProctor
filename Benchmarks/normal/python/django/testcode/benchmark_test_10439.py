# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest10439(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
