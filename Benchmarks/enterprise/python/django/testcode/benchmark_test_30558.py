# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import ast
from app_runtime import mq_client


def BenchmarkTest30558(request):
    msg_value = mq_client.get_message().body
    try:
        data = str(ast.literal_eval(msg_value))
    except (ValueError, SyntaxError):
        data = msg_value
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
