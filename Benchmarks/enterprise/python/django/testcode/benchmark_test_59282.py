# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest59282(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request.session['data'] = str(comment_value)
    return JsonResponse({"saved": True})
