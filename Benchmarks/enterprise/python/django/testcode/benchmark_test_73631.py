# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
import json
import ast


def BenchmarkTest73631(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.post('http://api.prod.internal/data', data=str(processed))
    return JsonResponse({"saved": True})
