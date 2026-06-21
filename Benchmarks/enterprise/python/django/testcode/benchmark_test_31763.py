# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest31763(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
