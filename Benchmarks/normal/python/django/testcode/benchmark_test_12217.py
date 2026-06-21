# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def BenchmarkTest12217(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % (json_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    values = str(processed).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
