# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest33301(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    prefix = ''
    data = prefix + str(json_value)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
