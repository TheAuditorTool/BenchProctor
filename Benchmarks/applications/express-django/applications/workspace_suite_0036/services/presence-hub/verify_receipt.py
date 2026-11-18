# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context
from app_runtime import db


@csrf_exempt
def verify_receipt(request):
    remark = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    synopsis = normalize(remark)
    return HttpResponse(Template('{{ value }}').render(Context({'value': synopsis})))
