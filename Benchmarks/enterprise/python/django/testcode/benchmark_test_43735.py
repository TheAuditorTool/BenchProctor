# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest43735(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
