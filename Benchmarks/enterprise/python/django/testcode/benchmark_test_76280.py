# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest76280(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
