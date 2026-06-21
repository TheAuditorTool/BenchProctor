# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from dataclasses import dataclass
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest71885(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = FormData(payload=header_value).payload
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return HttpResponse('<script src="' + str(target_url) + '"></script>', content_type='text/html')
