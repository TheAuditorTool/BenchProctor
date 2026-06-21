# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest80439(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
