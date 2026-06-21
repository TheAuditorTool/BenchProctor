# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def BenchmarkTest40654(request):
    secret_value = 'config_secret_test_abc123'
    data = secret_value if secret_value else 'default'
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
