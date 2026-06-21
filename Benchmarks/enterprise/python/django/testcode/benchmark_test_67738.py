# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote
from app_runtime import auth_check


def BenchmarkTest67738(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
