# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import re
from types import SimpleNamespace


def BenchmarkTest80618(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
