# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest49337(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
