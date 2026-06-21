# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest09488(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return HttpResponse('<script src="' + str(comment_value) + '"></script>', content_type='text/html')
