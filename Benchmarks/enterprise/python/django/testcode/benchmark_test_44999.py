# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from django.http import HttpResponse


def BenchmarkTest44999(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parsed = urlparse(origin_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = origin_value
    return HttpResponse('<script src="' + str(target_url) + '"></script>', content_type='text/html')
