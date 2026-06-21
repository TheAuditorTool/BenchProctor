# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import re


def BenchmarkTest35286(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return redirect(str(processed))
