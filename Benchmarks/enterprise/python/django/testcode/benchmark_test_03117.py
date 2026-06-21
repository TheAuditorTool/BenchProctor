# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from app_runtime import db


def BenchmarkTest03117(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    yaml.safe_load(comment_value)
    return JsonResponse({"saved": True})
