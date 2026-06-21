# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest00437(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    random.seed(int(header_value) if str(header_value).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
