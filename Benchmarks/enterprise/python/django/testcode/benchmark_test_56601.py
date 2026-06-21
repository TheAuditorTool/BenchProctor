# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest56601(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
