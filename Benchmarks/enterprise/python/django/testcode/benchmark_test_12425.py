# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest12425(request):
    user_id = request.GET.get('id', '')
    data = default_blank(user_id)
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JsonResponse({'token': str(token)}, status=200)
