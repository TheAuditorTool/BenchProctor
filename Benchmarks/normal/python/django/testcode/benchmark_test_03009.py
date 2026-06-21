# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest03009(request):
    raw_body = request.body.decode('utf-8')
    random.seed(int(raw_body) if str(raw_body).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
