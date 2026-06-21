# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest76960(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % (comment_value,)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
