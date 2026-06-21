# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from app_runtime import auth_check


def BenchmarkTest02539(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
