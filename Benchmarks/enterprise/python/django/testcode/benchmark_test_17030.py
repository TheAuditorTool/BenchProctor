# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import requests


def BenchmarkTest17030(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    def normalize(value):
        return value.strip()
    data = normalize(api_value)
    return redirect(str(data))
