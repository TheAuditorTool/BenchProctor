# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest34606(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(forwarded_ip).encode()))
    return JsonResponse({"saved": True})
