# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import keyring
from app_runtime import auth_check


def BenchmarkTest14797(request):
    secret_value = 'default_config_label'
    data = f'{secret_value:.200s}'
    store_cred = keyring.get_password('app', 'service-account')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
