# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest21395(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
