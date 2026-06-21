# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest19798(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    requests.get('https://api.pycdn.io/data', params={'q': str(comment_value)}, verify=True)
    return JsonResponse({"saved": True})
