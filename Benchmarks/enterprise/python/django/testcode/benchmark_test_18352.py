# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest18352(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
