# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def coalesce_blank(value):
    return value or ''

def BenchmarkTest07717(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = coalesce_blank(auth_header)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
