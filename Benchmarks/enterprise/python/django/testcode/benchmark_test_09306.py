# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest09306(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    random.seed(int(referer_value) if str(referer_value).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
