# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest38763(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
