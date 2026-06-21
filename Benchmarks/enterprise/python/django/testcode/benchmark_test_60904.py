# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest60904(request, path_param):
    path_value = path_param
    return HttpResponse(mark_safe('<img src="' + str(path_value) + '">'))
