# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast


def BenchmarkTest39216(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
