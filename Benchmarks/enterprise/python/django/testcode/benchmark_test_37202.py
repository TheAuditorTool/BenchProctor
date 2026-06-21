# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest37202(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data, _sep, _rest = str(dotenv_value).partition('\x00')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
