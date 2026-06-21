# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib
from app_runtime import db


def BenchmarkTest27896(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
