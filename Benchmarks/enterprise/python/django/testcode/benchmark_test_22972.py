# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import os


def BenchmarkTest22972(request):
    secret_value = 'default_config_label'
    data = (lambda v: v.strip())(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
