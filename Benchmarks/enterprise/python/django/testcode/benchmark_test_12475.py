# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote
from app_runtime import auth_check


def BenchmarkTest12475(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
