# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest18408(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    return HttpResponse(Template(data).render(Context()))
