# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest65072(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
