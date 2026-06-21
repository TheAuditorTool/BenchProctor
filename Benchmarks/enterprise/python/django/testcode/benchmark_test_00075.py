# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import keyring
from types import SimpleNamespace


def BenchmarkTest00075(request):
    secret_value = 'default_setting_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
