# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest53252(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
