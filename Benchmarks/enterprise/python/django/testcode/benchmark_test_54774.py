# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest54774(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    return HttpResponse(Template(data).render(Context()))
