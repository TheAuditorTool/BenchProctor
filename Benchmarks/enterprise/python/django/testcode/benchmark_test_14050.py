# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest14050(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
