# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from app_runtime import db


def BenchmarkTest21053(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
