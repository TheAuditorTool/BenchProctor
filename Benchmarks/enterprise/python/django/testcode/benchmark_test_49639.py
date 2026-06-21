# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest49639(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
