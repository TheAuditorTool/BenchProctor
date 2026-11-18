# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context
from app_runtime import db


@csrf_exempt
def summarize_threshold(request):
    subject = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    ledger = normalize(subject)
    return HttpResponse(Template('{{ value }}').render(Context({'value': ledger})))
