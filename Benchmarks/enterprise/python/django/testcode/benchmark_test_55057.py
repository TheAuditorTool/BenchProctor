# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def coalesce_blank(value):
    return value or ''

def BenchmarkTest55057(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
