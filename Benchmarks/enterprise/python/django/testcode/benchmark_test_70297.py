# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from app_runtime import db


def BenchmarkTest70297(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(comment_value)).read()
    return JsonResponse({"saved": True})
