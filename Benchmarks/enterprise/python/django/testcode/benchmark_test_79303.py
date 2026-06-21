# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


def BenchmarkTest79303(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(db_value)), context=ctx)
    return JsonResponse({"saved": True})
