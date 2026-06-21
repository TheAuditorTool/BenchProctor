# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest74354(request):
    cookie_value = request.COOKIES.get('session_token', '')
    random.seed(int(cookie_value) if str(cookie_value).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
