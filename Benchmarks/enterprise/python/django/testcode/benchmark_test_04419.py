# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import keyring
from app_runtime import auth_check


def BenchmarkTest04419(request):
    secret_value = 'feature_flag_value'
    data = '{}'.format(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
