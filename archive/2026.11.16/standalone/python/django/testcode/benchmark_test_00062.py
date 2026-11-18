# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db
from django.contrib.auth.models import User


def BenchmarkTest00062(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = []
    for token in str(comment_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
