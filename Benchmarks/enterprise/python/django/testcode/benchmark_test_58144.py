# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest58144(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    kind = 'json' if str(dotenv_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = dotenv_value
            data = parsed
        case _:
            data = dotenv_value
    auth_check('user', data)
    return JsonResponse({"saved": True})
