# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def BenchmarkTest02553(request):
    secret_value = 'config_secret_test_abc123'
    data = f'{secret_value:.200s}'
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
