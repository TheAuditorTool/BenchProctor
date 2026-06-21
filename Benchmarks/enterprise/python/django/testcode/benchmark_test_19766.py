# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest19766(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('/var/uploads/' + str(comment_value), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
