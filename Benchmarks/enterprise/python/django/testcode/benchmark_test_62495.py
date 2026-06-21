# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast
from app_runtime import auth_check


def BenchmarkTest62495(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
