# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest63672(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
