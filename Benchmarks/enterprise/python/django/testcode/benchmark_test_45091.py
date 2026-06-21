# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def BenchmarkTest45091(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ' '.join(str(json_value).split())
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
