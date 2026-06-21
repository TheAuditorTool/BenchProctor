# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import os


def BenchmarkTest46137(request):
    secret_value = 'default_setting_value'
    data = '%s' % str(secret_value)
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
