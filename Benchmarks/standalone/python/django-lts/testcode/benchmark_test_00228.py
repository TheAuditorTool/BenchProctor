# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00228(request):
    env_value = os.environ.get('APP_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
