# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import urllib.request


def BenchmarkTest79776(request):
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
