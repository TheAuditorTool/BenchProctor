# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


request_state: dict[str, str] = {}

def BenchmarkTest06300(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
