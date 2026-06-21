# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest57827(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    return HttpResponse(Template(data).render(Context()))
