# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import re


def normalise_input(value):
    return value.strip()

def BenchmarkTest03576(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return redirect(str(processed))
