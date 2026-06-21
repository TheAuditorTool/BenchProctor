# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from app_runtime import db


def BenchmarkTest30275(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
