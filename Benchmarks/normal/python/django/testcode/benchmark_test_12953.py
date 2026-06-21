# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest12953(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
