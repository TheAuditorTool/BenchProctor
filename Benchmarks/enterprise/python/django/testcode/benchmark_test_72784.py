# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def relay_value(value):
    return value

def BenchmarkTest72784(request):
    xml_value = request.body.decode('utf-8')
    data = relay_value(xml_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
