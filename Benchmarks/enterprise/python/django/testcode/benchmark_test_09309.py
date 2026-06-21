# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ast
import defusedxml.ElementTree


def BenchmarkTest09309(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
