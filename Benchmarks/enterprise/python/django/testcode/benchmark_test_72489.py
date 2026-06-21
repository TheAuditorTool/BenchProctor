# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest72489(request):
    raw_body = request.body.decode('utf-8')
    random.seed(int(raw_body) if str(raw_body).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
