# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest50114(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
