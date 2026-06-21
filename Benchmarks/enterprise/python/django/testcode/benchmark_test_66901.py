# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from django.http import HttpResponse


def BenchmarkTest66901(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parsed = urlparse(auth_header)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = auth_header
    return HttpResponse('<script src="' + str(target_url) + '"></script>', content_type='text/html')
