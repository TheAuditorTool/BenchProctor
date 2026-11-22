# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest00143(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
