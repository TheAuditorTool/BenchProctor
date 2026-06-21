# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest02845(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    def _primary():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
