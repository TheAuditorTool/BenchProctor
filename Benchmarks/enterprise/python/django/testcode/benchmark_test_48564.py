# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
import ast
from app_runtime import mq_client


def BenchmarkTest48564(request):
    msg_value = mq_client.get_message().body
    try:
        data = str(ast.literal_eval(msg_value))
    except (ValueError, SyntaxError):
        data = msg_value
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
