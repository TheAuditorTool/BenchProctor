# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest06626(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = '%s' % str(secret_value)
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return JsonResponse({"saved": True})
