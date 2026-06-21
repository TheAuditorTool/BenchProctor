# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest81422(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    random.seed(int(auth_header) if str(auth_header).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
