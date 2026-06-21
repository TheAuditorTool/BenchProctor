# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import keyring


def normalise_input(value):
    return value.strip()

def BenchmarkTest03246(request):
    secret_value = 'default_config_label'
    data = normalise_input(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
