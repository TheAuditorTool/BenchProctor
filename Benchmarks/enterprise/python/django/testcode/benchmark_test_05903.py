# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest05903(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = str(ast.literal_eval(config_value))
    except (ValueError, SyntaxError):
        data = config_value
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
