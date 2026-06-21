# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest33180(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json_value if json_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
