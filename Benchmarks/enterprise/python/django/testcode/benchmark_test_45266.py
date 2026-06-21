# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest45266(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
