# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def ensure_str(value):
    return str(value)

def BenchmarkTest23283(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ensure_str(forwarded_ip)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
