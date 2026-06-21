# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def BenchmarkTest79605(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
