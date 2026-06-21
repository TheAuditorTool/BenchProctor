# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest12401(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    random.seed(int(forwarded_ip) if str(forwarded_ip).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
