# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import ast


def BenchmarkTest51963(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
