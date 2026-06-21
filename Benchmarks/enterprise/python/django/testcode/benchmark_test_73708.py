# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from app_runtime import auth_check


def BenchmarkTest73708(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    if not auth_check(request.session.get('user', ''), str(data)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
