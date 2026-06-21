# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest44164(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
