# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest16059(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
