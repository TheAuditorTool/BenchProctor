# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def normalise_input(value):
    return value.strip()

def BenchmarkTest61578(request):
    raw_body = request.body.decode('utf-8')
    data = normalise_input(raw_body)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
