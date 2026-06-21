# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import yaml


def BenchmarkTest68504(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data, _sep, _rest = str(yaml_value).partition('\x00')
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
