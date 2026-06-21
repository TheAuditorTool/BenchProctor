# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest06435(request):
    host_value = request.META.get('HTTP_HOST', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(host_value), store_cred)
    return JsonResponse({"saved": True})
