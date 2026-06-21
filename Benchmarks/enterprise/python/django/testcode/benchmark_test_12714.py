# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest12714(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
