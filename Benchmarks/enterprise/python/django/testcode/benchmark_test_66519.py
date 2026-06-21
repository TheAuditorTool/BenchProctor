# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest66519(request):
    user_id = request.GET.get('id', '')
    data = ensure_str(user_id)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
