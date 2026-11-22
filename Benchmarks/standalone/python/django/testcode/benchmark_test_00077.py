# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest00077(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    digest = hashlib.sha3_256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
