# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import keyring
from app_runtime import db


def BenchmarkTest75848(request):
    secret_value = 'app_display_name'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return JsonResponse({"saved": True})
