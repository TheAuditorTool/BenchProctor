# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import json


def BenchmarkTest06247(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    return HttpResponse(Template(data).render(Context()))
