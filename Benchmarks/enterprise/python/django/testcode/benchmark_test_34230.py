# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def BenchmarkTest34230(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
