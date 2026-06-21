# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest09023(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % str(json_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
