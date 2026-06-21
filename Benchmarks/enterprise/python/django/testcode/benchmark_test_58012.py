# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest58012(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    reader = make_reader(secret_value)
    data = reader()
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
