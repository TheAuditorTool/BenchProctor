# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest43682(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return HttpResponse(Template(db_value).render(Context()))
