# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest28713(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return HttpResponse(Template(data).render(Context()))
