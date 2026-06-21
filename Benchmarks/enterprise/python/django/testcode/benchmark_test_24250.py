# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


request_state: dict[str, str] = {}

def BenchmarkTest24250(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
