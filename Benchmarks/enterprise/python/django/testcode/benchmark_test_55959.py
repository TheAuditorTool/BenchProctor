# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest55959(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
