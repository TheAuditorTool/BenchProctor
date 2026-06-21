# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest01239(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    return HttpResponse(Template(data).render(Context()))
