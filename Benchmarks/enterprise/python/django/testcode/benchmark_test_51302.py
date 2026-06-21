# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def BenchmarkTest51302(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
