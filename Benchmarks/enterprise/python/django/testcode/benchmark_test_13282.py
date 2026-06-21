# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest13282(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    return JsonResponse({'error': str(json_value), 'stack': repr(locals())}, status=500)
