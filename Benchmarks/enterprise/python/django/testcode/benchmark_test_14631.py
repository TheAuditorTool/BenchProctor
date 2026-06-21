# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14631(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    return HttpResponse(Template(data).render(Context()))
