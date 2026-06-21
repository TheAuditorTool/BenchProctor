# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest42142(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    random.seed(int(forwarded_ip) if str(forwarded_ip).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
