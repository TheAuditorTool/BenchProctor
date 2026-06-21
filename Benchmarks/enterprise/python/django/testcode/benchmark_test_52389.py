# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


request_state: dict[str, str] = {}

def BenchmarkTest52389(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
