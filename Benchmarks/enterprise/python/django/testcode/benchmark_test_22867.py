# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest22867(request):
    host_value = request.META.get('HTTP_HOST', '')
    random.seed(int(host_value) if str(host_value).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
