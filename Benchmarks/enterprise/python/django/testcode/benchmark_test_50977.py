# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest50977(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, comment_value))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
