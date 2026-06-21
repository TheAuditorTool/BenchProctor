# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest19913(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
