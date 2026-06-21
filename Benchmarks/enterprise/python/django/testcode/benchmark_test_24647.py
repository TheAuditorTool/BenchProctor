# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json


def BenchmarkTest24647(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
