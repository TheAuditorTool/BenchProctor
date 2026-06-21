# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest40733(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return JsonResponse({"saved": True})
