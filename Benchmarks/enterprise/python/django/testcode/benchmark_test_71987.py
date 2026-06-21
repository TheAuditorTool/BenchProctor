# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest71987(request):
    host_value = request.META.get('HTTP_HOST', '')
    random.seed(int(host_value) if str(host_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
