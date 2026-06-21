# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import keyring


def BenchmarkTest71641(request):
    secret_value = 'feature_flag_value'
    data = f'{secret_value:.200s}'
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
