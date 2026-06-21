# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest03670(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
