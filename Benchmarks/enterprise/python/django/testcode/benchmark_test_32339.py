# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest32339(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
