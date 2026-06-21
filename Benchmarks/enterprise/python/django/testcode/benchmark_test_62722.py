# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import defusedxml.ElementTree


request_state: dict[str, str] = {}

def BenchmarkTest62722(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
