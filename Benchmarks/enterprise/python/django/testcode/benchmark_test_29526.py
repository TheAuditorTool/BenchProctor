# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
import json
import ast


def BenchmarkTest29526(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
