# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import base64


def BenchmarkTest48364(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
