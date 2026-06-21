# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


def BenchmarkTest51789(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
