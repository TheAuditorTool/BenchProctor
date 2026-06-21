# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import socket


def BenchmarkTest57916(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = api_value if api_value else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
