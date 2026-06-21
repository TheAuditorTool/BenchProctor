# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import ast


def BenchmarkTest35021(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
