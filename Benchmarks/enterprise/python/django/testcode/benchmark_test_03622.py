# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def relay_value(value):
    return value

def BenchmarkTest03622(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
