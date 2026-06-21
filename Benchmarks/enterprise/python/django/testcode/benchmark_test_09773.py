# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest09773(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
