# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest46830(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    random.seed(int(ua_value) if str(ua_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
