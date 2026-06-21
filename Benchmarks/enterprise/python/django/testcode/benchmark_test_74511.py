# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from django.http import HttpResponse


def BenchmarkTest74511(request):
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
