# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00275(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
