# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest53688(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JsonResponse({'token': str(token)}, status=200)
