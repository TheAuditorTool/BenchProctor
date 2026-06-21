# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest61302(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(dotenv_value), store_cred)
    return JsonResponse({"saved": True})
