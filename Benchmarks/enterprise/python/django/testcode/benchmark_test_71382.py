# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest71382(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(header_value), store_cred)
    return JsonResponse({"saved": True})
