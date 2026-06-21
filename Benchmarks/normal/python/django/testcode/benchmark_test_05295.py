# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest05295(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return HttpResponse(mark_safe('<div>' + str(db_value) + '</div>'))
