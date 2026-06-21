# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest71169(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
