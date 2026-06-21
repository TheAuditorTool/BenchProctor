# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from django.http import HttpResponse


def BenchmarkTest40171(request):
    xml_value = request.body.decode('utf-8')
    parsed = urlparse(xml_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = xml_value
    return HttpResponse('<script src="' + str(target_url) + '"></script>', content_type='text/html')
