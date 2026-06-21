# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest25771(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    os.remove(str(data))
    return JsonResponse({"saved": True})
