# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest05927(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
