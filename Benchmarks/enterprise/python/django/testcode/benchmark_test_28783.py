# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest28783(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return JsonResponse({"saved": True})
