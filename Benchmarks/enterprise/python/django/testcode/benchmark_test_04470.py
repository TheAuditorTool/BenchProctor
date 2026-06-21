# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest04470(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        os.setuid(int(str(comment_value)) if str(comment_value).isdigit() else 65534)
    except OSError:
        pass
    return JsonResponse({"saved": True})
