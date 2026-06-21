# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def BenchmarkTest75118(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = ' '.join(str(secret_value).split())
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
