# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import re
from types import SimpleNamespace


def BenchmarkTest64591(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
