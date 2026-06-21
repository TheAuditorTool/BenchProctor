# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def to_text(value):
    return str(value).strip()

def BenchmarkTest61970(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = to_text(ua_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
