# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import pickle


def BenchmarkTest68411(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = (lambda v: v.strip())(api_value)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
