# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from types import SimpleNamespace


def BenchmarkTest26565(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return JsonResponse({"saved": True})
