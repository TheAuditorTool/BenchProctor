# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest08714(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return JsonResponse({"saved": True})
