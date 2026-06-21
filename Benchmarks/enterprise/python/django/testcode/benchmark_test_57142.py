# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest57142(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    requests.post('http://api.prod.internal/data', data=str(comment_value))
    return JsonResponse({"saved": True})
