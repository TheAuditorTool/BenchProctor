# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from app_runtime import db


def BenchmarkTest00576(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    pending = list(str(comment_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
