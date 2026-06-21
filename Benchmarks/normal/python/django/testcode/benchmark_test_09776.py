# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest09776(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
