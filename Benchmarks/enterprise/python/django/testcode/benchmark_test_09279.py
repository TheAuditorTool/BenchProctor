# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest09279(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
