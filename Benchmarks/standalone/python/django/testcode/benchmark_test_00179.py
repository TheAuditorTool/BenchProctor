# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64
import pickle


def BenchmarkTest00179(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = '{}'.format(api_value)
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
