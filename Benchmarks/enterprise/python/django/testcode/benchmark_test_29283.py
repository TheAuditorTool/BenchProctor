# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest29283(request):
    raw_body = request.body.decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', raw_body):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = raw_body
    eval(str(processed))
    return JsonResponse({"saved": True})
