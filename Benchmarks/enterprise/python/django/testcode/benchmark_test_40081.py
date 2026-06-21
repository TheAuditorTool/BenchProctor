# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest40081(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(comment_value))
    return JsonResponse({"saved": True})
