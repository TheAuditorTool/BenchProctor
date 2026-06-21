# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest62390(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = to_text(forwarded_ip)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
