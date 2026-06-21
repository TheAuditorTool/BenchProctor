# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest70407(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    digest = hashlib.md5(str(json_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
