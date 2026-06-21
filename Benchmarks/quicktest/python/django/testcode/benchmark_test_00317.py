# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00317(request):
    secret_value = 'config_secret_test_abc123'
    reader = make_reader(secret_value)
    data = reader()
    auth_check('user', data)
    return JsonResponse({"saved": True})
