# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def relay_value(value):
    return value

def BenchmarkTest01270(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = relay_value(ua_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
