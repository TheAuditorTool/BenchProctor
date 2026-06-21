# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json


def BenchmarkTest08252(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
