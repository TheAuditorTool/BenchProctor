# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest77907(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
