# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest19175(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = default_blank(header_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return JsonResponse({"saved": True})
