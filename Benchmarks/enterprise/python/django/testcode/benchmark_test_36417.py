# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest36417(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': data})))
