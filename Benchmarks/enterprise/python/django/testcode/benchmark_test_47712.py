# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json
import ast


def BenchmarkTest47712(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    processed = re.sub(r'\d+', '****', str(data))
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
