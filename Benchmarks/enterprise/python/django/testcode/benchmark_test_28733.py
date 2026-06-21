# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest28733(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(forwarded_ip)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = forwarded_ip
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
