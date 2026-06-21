# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest24258(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = f'{dotenv_value:.200s}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
