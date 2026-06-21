# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest30219(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
