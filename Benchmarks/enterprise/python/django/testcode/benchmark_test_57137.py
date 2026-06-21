# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest57137(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
