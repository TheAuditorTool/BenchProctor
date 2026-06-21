# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json
from django.http import HttpResponse


def BenchmarkTest02513(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
