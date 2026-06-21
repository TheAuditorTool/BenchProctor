# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from app_runtime import db


def BenchmarkTest01448(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ','.join(parts)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
