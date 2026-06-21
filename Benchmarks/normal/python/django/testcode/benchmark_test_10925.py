# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest10925(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return HttpResponse(Template(comment_value).render(Context()))
