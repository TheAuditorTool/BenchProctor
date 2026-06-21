# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest36162(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
