# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest68056(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return HttpResponse(Template(data).render(Context()))
