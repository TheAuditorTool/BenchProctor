# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import json


def BenchmarkTest17640(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    return HttpResponse(Template(json_value).render(Context()))
