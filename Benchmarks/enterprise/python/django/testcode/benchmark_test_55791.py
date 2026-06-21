# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest55791(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    os.chmod('/var/app/data/' + str(comment_value), 0o777)
    return JsonResponse({"saved": True})
