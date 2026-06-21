# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest17303(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
