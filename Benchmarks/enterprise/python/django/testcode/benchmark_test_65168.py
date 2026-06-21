# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote
from app_runtime import auth_check


def BenchmarkTest65168(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
