# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest56201(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    kind = 'json' if str(config_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = config_value
            data = parsed
        case _:
            data = config_value
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
