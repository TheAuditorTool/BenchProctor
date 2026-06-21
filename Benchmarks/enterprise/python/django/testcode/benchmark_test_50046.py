# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest50046(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
