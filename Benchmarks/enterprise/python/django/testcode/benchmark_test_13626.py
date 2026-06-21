# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest13626(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = f'{dotenv_value}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
