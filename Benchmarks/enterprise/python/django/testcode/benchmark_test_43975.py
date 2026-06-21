# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import keyring


def BenchmarkTest43975(request):
    secret_value = 'app_display_name'
    data = (lambda v: v.strip())(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
