# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest26645(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
