# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest80031(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
