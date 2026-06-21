# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
import ast
from app_runtime import auth_check


def BenchmarkTest12293(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return JsonResponse({"saved": True})
