# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ast
from app_runtime import auth_check


def BenchmarkTest62241(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
