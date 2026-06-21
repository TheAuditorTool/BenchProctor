# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
import ast


def BenchmarkTest08094(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
