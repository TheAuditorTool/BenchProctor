# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context
from app_runtime import db


@csrf_exempt
def format_report(request):
    tagline = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    rendition = normalize(tagline)
    return HttpResponse(Template('{{ value }}').render(Context({'value': rendition})))
