# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
import ast


def BenchmarkTest22284(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
