# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest79266(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = '{}'.format(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
