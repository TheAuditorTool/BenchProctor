# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest03278(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
