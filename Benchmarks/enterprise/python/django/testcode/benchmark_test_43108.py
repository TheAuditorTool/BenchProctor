# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest43108(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value:.200s}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
