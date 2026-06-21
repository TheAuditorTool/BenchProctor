# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest05374(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    processed = data[:64]
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
