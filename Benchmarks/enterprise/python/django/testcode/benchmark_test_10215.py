# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
from app_runtime import db


def BenchmarkTest10215(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
