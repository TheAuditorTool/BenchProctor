# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def relay_value(value):
    return value

def BenchmarkTest58036(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = relay_value(referer_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
