# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest71705(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return HttpResponse(Template(data).render(Context()))
