# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import base64


def BenchmarkTest04634(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
