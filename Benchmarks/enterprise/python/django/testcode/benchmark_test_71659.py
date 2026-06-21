# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest71659(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = coalesce_blank(secret_value)
    processed = data[:64]
    auth_check('user', processed)
    return JsonResponse({"saved": True})
