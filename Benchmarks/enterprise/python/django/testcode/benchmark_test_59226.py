# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def normalise_input(value):
    return value.strip()

def BenchmarkTest59226(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
