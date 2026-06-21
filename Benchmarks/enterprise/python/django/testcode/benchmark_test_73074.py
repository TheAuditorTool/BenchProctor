# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import requests


def BenchmarkTest73074(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = json.loads(api_value).get('value', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
