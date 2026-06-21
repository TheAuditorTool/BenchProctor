# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def BenchmarkTest12337(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(json_value).replace('\r', '').replace('\n', ''))
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
