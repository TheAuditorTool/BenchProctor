# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
import ast


def BenchmarkTest69895(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = str(ast.literal_eval(dotenv_value))
    except (ValueError, SyntaxError):
        data = dotenv_value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
