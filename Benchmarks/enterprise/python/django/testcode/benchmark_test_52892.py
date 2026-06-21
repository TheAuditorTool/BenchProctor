# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def BenchmarkTest52892(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
