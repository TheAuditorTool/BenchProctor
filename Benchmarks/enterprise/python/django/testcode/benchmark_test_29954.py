# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def BenchmarkTest29954(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JsonResponse({'token': str(token)}, status=200)
