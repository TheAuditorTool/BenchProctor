# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest56549(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
