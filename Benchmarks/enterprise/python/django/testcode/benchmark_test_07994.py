# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest07994(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
