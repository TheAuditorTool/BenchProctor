# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest08112(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    random.seed(int(forwarded_ip) if str(forwarded_ip).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
