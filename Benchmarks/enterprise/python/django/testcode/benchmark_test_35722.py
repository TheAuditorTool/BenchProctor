# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest35722(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = relay_value(comment_value)
    os.seteuid(65534)
    return JsonResponse({"saved": True})
