# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest79029(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
