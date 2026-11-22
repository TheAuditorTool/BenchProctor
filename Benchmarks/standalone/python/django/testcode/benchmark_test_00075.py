# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import SHA256
import json


def BenchmarkTest00075(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = json_value if json_value else 'default'
    digest = SHA256.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
