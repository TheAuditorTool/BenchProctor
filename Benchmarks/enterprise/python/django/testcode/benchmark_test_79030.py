# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


request_state: dict[str, str] = {}

def BenchmarkTest79030(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    processed = data[:64]
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
