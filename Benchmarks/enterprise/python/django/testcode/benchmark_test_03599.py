# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import re


def BenchmarkTest03599(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
