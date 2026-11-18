# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00529(request):
    env_value = os.environ.get('APP_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(env_value).strip()
        case _:
            data = str(env_value)
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
