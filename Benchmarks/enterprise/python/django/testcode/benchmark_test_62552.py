# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from app_runtime import db


def BenchmarkTest62552(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
