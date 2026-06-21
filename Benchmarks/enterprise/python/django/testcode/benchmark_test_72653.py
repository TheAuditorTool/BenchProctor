# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest72653(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/www/html/exports/report.txt', 'wb') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return JsonResponse({"saved": True})
