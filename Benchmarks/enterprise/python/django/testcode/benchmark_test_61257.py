# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest61257(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
