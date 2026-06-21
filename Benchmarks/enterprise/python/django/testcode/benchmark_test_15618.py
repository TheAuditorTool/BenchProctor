# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest15618(request):
    user_id = request.GET.get('id', '')
    random.seed(int(user_id) if str(user_id).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
