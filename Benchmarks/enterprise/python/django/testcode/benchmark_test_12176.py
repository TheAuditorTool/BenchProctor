# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest12176(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
