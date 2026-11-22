# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest00154(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
