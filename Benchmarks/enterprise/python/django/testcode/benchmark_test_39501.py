# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import ast


def BenchmarkTest39501(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    os.remove(str(data))
    return JsonResponse({"saved": True})
