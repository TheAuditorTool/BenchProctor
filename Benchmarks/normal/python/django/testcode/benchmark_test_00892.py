# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00892(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
