# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os
from app_runtime import db


def BenchmarkTest02974(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % (comment_value,)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
