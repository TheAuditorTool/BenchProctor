# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest48628(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
