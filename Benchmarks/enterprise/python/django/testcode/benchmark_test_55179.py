# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import ast


def BenchmarkTest55179(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
