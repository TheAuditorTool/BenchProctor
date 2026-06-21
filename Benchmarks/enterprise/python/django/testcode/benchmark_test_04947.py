# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest04947(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
