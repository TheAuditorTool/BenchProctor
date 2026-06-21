# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest21630(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if comment_value not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + comment_value
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
