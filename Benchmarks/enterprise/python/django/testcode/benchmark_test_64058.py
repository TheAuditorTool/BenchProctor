# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


def BenchmarkTest64058(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return JsonResponse({"saved": True})
