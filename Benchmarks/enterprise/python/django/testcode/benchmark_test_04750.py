# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from urllib.parse import unquote


def BenchmarkTest04750(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
