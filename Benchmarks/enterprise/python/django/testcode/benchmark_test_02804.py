# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02804(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': data})))
