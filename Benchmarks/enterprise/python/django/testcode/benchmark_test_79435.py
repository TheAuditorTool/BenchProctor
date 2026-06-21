# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.template import Template, Context
import json


def BenchmarkTest79435(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ' '.join(str(json_value).split())
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
