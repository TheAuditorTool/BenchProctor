# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from app_runtime import db


def BenchmarkTest33634(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
