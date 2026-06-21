# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest56060(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
