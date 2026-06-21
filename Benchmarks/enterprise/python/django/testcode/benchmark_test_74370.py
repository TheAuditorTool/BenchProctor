# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


request_state: dict[str, str] = {}

def BenchmarkTest74370(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
