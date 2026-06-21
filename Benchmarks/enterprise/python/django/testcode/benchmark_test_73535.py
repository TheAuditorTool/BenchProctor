# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest73535(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
