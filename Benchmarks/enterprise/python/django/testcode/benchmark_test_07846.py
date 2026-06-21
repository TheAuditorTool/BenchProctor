# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest07846(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = f'{secret_value}'
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
