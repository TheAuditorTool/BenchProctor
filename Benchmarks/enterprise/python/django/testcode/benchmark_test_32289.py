# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest32289(request):
    user_id = request.GET.get('id', '')
    random.seed(int(user_id) if str(user_id).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
