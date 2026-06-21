# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import ast


def BenchmarkTest77117(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
