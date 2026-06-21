# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import time


def to_text(value):
    return str(value).strip()

def BenchmarkTest57362(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    if time.time() > 1000000000:
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
