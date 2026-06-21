# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def BenchmarkTest61534(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    random.seed(int(json_value) if str(json_value).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
