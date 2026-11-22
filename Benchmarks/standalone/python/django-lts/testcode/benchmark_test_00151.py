# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import SHA256
import json
from app_runtime import db


def BenchmarkTest00151(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    digest = SHA256.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
