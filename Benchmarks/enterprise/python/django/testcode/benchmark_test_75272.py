# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest75272(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
