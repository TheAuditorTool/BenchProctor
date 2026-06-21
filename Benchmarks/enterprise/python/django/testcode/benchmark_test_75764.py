# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest75764(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return HttpResponse('<!-- diagnostic build token: ' + str(comment_value) + ' -->', content_type='text/html')
