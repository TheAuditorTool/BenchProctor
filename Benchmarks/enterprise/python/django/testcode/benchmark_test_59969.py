# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import re


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest59969(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return redirect(str(processed))
