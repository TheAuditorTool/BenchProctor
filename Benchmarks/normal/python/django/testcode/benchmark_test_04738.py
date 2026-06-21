# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re
import os


def BenchmarkTest04738(request):
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', env_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = env_value
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
