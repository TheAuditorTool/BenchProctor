# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
from django.template import Template, Context


def BenchmarkTest01765(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
