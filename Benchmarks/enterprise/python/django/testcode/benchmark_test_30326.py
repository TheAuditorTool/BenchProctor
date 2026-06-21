# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def to_text(value):
    return str(value).strip()

def BenchmarkTest30326(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = to_text(multipart_value)
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JsonResponse({'token': str(token)}, status=200)
