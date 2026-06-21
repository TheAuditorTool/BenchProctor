# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest35130(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
