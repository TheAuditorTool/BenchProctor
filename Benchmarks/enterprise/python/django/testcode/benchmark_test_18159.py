# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest18159(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    digest = hashlib.sha1(str(graphql_var).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
