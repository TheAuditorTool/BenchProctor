# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest30766(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % (comment_value,)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
