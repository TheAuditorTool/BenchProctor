# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest09611(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
