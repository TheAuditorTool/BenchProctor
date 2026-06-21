# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


request_state: dict[str, str] = {}

def BenchmarkTest42063(request):
    host_value = request.META.get('HTTP_HOST', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
