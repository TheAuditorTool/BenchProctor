# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest37502(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return HttpResponse('<script src="' + str(db_value) + '"></script>', content_type='text/html')
