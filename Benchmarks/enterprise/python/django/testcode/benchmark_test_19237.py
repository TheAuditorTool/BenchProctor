# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest19237(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    random.seed(int(referer_value) if str(referer_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
