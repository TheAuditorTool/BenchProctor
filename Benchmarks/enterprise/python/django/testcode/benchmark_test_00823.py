# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def BenchmarkTest00823(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data, _sep, _rest = str(secret_value).partition('\x00')
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
