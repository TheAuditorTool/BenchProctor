# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from urllib.parse import unquote


def BenchmarkTest25823(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    return HttpResponse(Template(data).render(Context()))
