# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def BenchmarkTest39640(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json.loads(json_value).get('value', '')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
