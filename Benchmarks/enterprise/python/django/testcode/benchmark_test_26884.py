# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest26884(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = '{}'.format(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
