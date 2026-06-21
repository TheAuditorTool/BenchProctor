# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest10526(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
