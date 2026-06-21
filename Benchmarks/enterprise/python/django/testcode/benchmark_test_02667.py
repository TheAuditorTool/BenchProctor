# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import keyring


def BenchmarkTest02667(request):
    secret_value = 'default_config_label'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
