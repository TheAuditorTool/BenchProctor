# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00146(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    code = compile(str(data), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
