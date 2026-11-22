# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from django.template import Template, Context
from app_runtime import db


def BenchmarkTest00080(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(data)}))
    return HttpResponse(page)
