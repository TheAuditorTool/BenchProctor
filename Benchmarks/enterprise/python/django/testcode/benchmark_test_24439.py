# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def coalesce_blank(value):
    return value or ''

def BenchmarkTest24439(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
