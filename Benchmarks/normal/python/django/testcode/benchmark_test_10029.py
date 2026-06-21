# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import re


def ensure_str(value):
    return str(value)

def BenchmarkTest10029(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ensure_str(header_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return redirect(str(processed))
