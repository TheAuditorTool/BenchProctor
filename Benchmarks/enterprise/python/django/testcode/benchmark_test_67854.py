# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest67854(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
