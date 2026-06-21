# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import json


def BenchmarkTest41214(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': json_value})))
