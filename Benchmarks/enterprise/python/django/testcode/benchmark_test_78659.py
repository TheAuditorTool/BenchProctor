# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import re


def BenchmarkTest78659(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
