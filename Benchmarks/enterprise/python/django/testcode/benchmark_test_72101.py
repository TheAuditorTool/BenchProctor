# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest72101(request):
    user_id = request.GET.get('id', '')
    data = default_blank(user_id)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
