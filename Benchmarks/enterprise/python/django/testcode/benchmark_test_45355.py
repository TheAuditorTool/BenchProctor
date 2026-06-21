# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest45355(request):
    raw_body = request.body.decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
