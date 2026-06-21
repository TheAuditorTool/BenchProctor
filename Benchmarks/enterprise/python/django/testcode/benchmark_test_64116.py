# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest64116(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    os.seteuid(65534)
    return JsonResponse({"saved": True})
