# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import ast
import subprocess


def BenchmarkTest69426(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = str(ast.literal_eval(graphql_var))
    except (ValueError, SyntaxError):
        data = graphql_var
    eval(compile("subprocess.run([str(data), '--status'], shell=False)", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
