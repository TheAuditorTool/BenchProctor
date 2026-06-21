# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest08537(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    json.loads(data)
    return JsonResponse({"saved": True})
