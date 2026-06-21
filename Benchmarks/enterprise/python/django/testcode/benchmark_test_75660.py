# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import ast
import socket


def BenchmarkTest75660(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return JsonResponse({"saved": True})
