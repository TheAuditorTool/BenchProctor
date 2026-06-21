# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest79066(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
