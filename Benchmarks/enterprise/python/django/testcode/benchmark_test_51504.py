# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51504(request, path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    processed = data[:64]
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed))
    return resp
