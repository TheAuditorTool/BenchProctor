# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import ast


def BenchmarkTest76754(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
