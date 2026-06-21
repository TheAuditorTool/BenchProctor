# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest02693(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return HttpResponse('<script src="' + str(target_url) + '"></script>', content_type='text/html')
