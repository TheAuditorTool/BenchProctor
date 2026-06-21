# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest62222(request):
    xml_value = request.body.decode('utf-8')
    data = handle(xml_value)
    processed = data[:64]
    return redirect(str(processed))
