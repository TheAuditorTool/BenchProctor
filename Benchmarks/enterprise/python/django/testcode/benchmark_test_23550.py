# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
import ast


def BenchmarkTest23550(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
