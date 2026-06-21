# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest30033(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ensure_str(json_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
