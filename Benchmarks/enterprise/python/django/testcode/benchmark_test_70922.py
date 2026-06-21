# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os
from django.http import HttpResponse


def BenchmarkTest70922(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
