# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import pickle


def BenchmarkTest78274(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = str(api_value).replace('\x00', '')
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
