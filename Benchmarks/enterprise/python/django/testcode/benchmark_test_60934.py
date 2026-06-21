# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random


def BenchmarkTest60934(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
