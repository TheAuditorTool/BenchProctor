# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest51266(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
