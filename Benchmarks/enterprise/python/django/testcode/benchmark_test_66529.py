# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from types import SimpleNamespace


def BenchmarkTest66529(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return JsonResponse({"saved": True})
