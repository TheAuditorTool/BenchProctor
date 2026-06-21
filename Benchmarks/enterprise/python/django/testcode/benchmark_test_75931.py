# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from django.http import HttpResponse
import json


def BenchmarkTest75931(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return HttpResponse('<script src="' + str(target_url) + '"></script>', content_type='text/html')
