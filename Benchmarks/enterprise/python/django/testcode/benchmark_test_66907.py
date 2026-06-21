# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest66907(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return JsonResponse({"saved": True})
