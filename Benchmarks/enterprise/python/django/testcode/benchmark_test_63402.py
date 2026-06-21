# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest63402(request, path_param):
    path_value = path_param
    return HttpResponse(Template(path_value).render(Context()))
