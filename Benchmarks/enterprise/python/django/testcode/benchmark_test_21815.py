# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import os


def BenchmarkTest21815(request):
    secret_value = 'app_display_name'
    data = str(secret_value).replace('\x00', '')
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
