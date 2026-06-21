# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest34023(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    auth_check('user', dotenv_value)
    return JsonResponse({"saved": True})
