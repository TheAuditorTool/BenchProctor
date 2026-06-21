# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest80713(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
