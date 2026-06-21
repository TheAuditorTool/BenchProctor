# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from urllib.parse import unquote


def BenchmarkTest02370(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
