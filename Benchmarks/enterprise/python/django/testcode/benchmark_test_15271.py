# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import ast


def BenchmarkTest15271(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
