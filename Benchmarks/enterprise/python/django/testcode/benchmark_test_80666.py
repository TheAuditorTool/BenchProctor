# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest80666(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HttpResponse(Template(processed).render(Context()))
