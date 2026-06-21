# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import requests


def BenchmarkTest81293(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    parts = str(api_value).split(',')
    data = ','.join(parts)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
