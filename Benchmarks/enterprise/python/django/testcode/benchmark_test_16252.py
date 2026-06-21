# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def relay_value(value):
    return value

def BenchmarkTest16252(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = relay_value(auth_header)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
