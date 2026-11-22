# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from django.template import Template, Context
from app_runtime import db


def BenchmarkTest00067(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    resp = HttpResponse(content_type='text/html')
    resp.write(Template('<div>{{ value }}</div>').render(Context({'value': str(comment_value)})))
    return resp
