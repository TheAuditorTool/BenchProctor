# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest19436(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    random.seed(int(ua_value) if str(ua_value).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
