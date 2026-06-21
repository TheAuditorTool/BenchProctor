# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time
import ast


def BenchmarkTest76799(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
