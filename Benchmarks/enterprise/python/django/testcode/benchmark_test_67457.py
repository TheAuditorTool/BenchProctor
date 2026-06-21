# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os
from django.shortcuts import redirect
import urllib.parse


def BenchmarkTest67457(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
