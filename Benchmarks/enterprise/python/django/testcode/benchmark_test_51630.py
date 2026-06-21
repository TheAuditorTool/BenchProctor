# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest51630(request):
    raw_body = request.body.decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', raw_body):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = raw_body
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
