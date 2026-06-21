# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37242(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
