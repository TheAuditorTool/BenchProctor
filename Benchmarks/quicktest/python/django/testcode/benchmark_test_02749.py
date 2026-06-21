# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest02749(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
