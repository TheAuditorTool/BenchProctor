# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest51442(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    processed = 'true' if str(comment_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HttpResponse(Template(processed).render(Context()))
