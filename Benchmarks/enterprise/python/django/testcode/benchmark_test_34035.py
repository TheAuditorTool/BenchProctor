# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def ensure_str(value):
    return str(value)

def BenchmarkTest34035(request):
    user_id = request.GET.get('id', '')
    data = ensure_str(user_id)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
