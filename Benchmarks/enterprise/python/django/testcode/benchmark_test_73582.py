# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest73582(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
