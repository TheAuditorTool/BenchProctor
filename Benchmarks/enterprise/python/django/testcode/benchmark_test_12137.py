# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import json
from app_runtime import db


def BenchmarkTest12137(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': data})))
