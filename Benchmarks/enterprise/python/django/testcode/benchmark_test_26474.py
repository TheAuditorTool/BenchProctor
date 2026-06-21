# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest26474(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parsed = urlparse(comment_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = comment_value
    return HttpResponse('<script src="' + str(target_url) + '"></script>', content_type='text/html')
