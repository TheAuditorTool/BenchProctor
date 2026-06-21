# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest76826(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
