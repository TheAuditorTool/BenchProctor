# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.template import Template, Context
from app_runtime import db


def BenchmarkTest33765(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '{}'.format(comment_value)
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
