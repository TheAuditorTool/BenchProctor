# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest17077(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    os.remove(str(comment_value))
    return JsonResponse({"saved": True})
